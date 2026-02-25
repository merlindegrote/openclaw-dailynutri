#!/usr/bin/env python3
"""
DailyNutri OpenClaw Integratie
Integreert DailyNutri API met OpenClaw voor automatische food logging
"""

import os
import sys
import json
from datetime import datetime
from typing import Dict, List, Optional
from api_client import DailyNutriAPIClient

class OpenClawDailyNutriIntegration:
    """Integratie tussen OpenClaw en DailyNutri"""
    
    def __init__(self, api_key: str = None):
        """
        Initializeer OpenClaw integratie
        
        Args:
            api_key: DailyNutri API key
        """
        self.client = DailyNutriAPIClient(api_key)
        self.log_file = "/config/.openclaw/workspace/dailynutri/logs/food_log.json"
        
        # Maak logs directory aan
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
    
    def log_from_openclaw(self, food_description: str, context: str = None) -> Dict:
        """
        Log food vanuit OpenClaw met context
        
        Args:
            food_description: Beschrijving van food
            context: Optionele context (bijv. "breakfast", "lunch", "dinner", "snack")
        
        Returns:
            Dict met resultaat
        """
        timestamp = datetime.now().isoformat()
        
        try:
            # Voeg context toe aan beschrijving indien aanwezig
            if context:
                full_description = f"{context}: {food_description}"
            else:
                full_description = food_description
            
            # Log naar DailyNutri API
            api_result = self.client.log_food(full_description)
            
            # Sla lokaal op
            log_entry = {
                "timestamp": timestamp,
                "description": food_description,
                "context": context,
                "api_result": api_result,
                "success": api_result.get('action') == 'logged'
            }
            
            self._save_log_entry(log_entry)
            
            # Maak mooie response voor OpenClaw
            response = {
                "status": "success" if log_entry["success"] else "partial",
                "message": api_result.get('reply', '✅ Food gelogd'),
                "details": {
                    "items_logged": len(api_result.get('items', [])),
                    "total_calories": sum(item.get('calories', 0) for item in api_result.get('items', [])),
                    "meal_id": api_result.get('meal_id')
                },
                "log_entry": log_entry
            }
            
            return response
            
        except Exception as e:
            # Sla failed attempt ook op
            error_entry = {
                "timestamp": timestamp,
                "description": food_description,
                "context": context,
                "error": str(e),
                "success": False
            }
            
            self._save_log_entry(error_entry)
            
            return {
                "status": "error",
                "message": f"❌ Fout bij loggen: {str(e)}",
                "log_entry": error_entry
            }
    
    def query_from_openclaw(self, question: str) -> Dict:
        """
        Query vanuit OpenClaw
        
        Args:
            question: Vraag over voeding
        
        Returns:
            Dict met resultaat
        """
        try:
            result = self.client.query_food_history(question)
            
            return {
                "status": "success",
                "action": result.get('action', 'query'),
                "reply": result.get('reply', '⚠️ Geen antwoord ontvangen'),
                "raw_response": result
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Fout bij query: {str(e)}"
            }
    
    def get_daily_summary(self) -> Dict:
        """Haal dagelijkse samenvatting op"""
        try:
            result = self.client.get_today_summary()
            
            return {
                "status": "success",
                "summary": result.get('reply', '⚠️ Geen data voor vandaag'),
                "raw_response": result
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"❌ Fout bij ophalen samenvatting: {str(e)}"
            }
    
    def _save_log_entry(self, entry: Dict):
        """Sla log entry op in JSON file"""
        try:
            # Lees bestaande logs
            logs = []
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r') as f:
                    try:
                        logs = json.load(f)
                    except json.JSONDecodeError:
                        logs = []
            
            # Voeg nieuwe entry toe
            logs.append(entry)
            
            # Bewaar (laatste 100 entries)
            if len(logs) > 100:
                logs = logs[-100:]
            
            with open(self.log_file, 'w') as f:
                json.dump(logs, f, indent=2, default=str)
                
        except Exception as e:
            print(f"⚠️ Kon log entry niet opslaan: {e}")
    
    def get_log_history(self, limit: int = 10) -> List[Dict]:
        """Haal log geschiedenis op"""
        try:
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r') as f:
                    logs = json.load(f)
                return logs[-limit:] if limit else logs
            return []
        except Exception as e:
            print(f"⚠️ Kon log geschiedenis niet lezen: {e}")
            return []
    
    def generate_weekly_report(self) -> str:
        """Genereer wekelijkse rapportage"""
        logs = self.get_log_history(limit=50)  # Laatste 50 entries
        
        if not logs:
            return "📊 Geen food logs gevonden voor rapportage."
        
        successful_logs = [log for log in logs if log.get('success')]
        failed_logs = [log for log in logs if not log.get('success')]
        
        report = f"""📊 Weekly Food Log Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

📈 Statistics:
• Total logs: {len(logs)}
• Successful: {len(successful_logs)} ({len(successful_logs)/max(len(logs), 1)*100:.1f}%)
• Failed: {len(failed_logs)} ({len(failed_logs)/max(len(logs), 1)*100:.1f}%)

🍽️ Recent Successful Logs:"""
        
        for log in successful_logs[-5:]:  # Laatste 5 successen
            timestamp = log.get('timestamp', 'Unknown')
            desc = log.get('description', 'No description')[:50]
            report += f"\n• {timestamp}: {desc}"
        
        if failed_logs:
            report += "\n\n❌ Recent Failed Logs:"
            for log in failed_logs[-3:]:  # Laatste 3 failures
                timestamp = log.get('timestamp', 'Unknown')
                error = log.get('error', 'Unknown error')[:50]
                report += f"\n• {timestamp}: {error}"
        
        report += "\n\n💡 Tips:"
        report += "\n• Gebruik specifieke beschrijvingen (150g kip ipv kip)"
        report += "\n• Log direct na het eten voor betere tracking"
        report += "\n• Gebruik context (breakfast, lunch, dinner, snack)"
        
        return report


# Eenvoudige wrapper functies voor OpenClaw
def log_food_openclaw(food_description: str, context: str = None, api_key: str = None) -> Dict:
    """Log food vanuit OpenClaw"""
    integrator = OpenClawDailyNutriIntegration(api_key)
    return integrator.log_from_openclaw(food_description, context)

def query_food_openclaw(question: str, api_key: str = None) -> Dict:
    """Query food vanuit OpenClaw"""
    integrator = OpenClawDailyNutriIntegration(api_key)
    return integrator.query_from_openclaw(question)

def get_daily_summary_openclaw(api_key: str = None) -> Dict:
    """Haal dagelijkse samenvatting op"""
    integrator = OpenClawDailyNutriIntegration(api_key)
    return integrator.get_daily_summary()


if __name__ == "__main__":
    """Test de OpenClaw integratie"""
    import sys
    
    def print_usage():
        print("Usage: python openclaw_integration.py <command> [args]")
        print("\nCommands:")
        print("  log <description> [context] - Log food")
        print("  query <question>            - Stel vraag")
        print("  summary                     - Dagelijkse samenvatting")
        print("  history [limit]             - Toon log geschiedenis")
        print("  report                      - Genereer wekelijks rapport")
        print("\nVoorbeeld:")
        print('  python openclaw_integration.py log "Ik heb een appel gegeten" breakfast')
        print('  python openclaw_integration.py query "Wat heb ik gisteren gegeten?"')
        print('  python openclaw_integration.py summary')
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    try:
        integrator = OpenClawDailyNutriIntegration()
        
        if command == "log" and len(sys.argv) >= 3:
            description = sys.argv[2]
            context = sys.argv[3] if len(sys.argv) >= 4 else None
            result = integrator.log_from_openclaw(description, context)
            print(json.dumps(result, indent=2, default=str))
        
        elif command == "query" and len(sys.argv) >= 3:
            question = ' '.join(sys.argv[2:])
            result = integrator.query_from_openclaw(question)
            print(json.dumps(result, indent=2, default=str))
        
        elif command == "summary":
            result = integrator.get_daily_summary()
            print(json.dumps(result, indent=2, default=str))
        
        elif command == "history":
            limit = int(sys.argv[2]) if len(sys.argv) >= 3 else 10
            history = integrator.get_log_history(limit)
            print(json.dumps(history, indent=2, default=str))
        
        elif command == "report":
            report = integrator.generate_weekly_report()
            print(report)
        
        else:
            print_usage()
    
    except Exception as e:
        print(f"❌ Fout: {e}")
        sys.exit(1)