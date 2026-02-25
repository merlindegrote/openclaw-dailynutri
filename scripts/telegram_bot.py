#!/usr/bin/env python3
"""
DailyNutri Telegram Bot Integratie
Laat je food loggen via Telegram berichten
"""

import os
import sys
import json
from typing import Dict, Optional
from api_client import DailyNutriAPIClient, log_food, query_food

class DailyNutriTelegramBot:
    """Integratie tussen DailyNutri API en Telegram"""
    
    def __init__(self, api_key: str = None):
        """
        Initializeer de Telegram bot integratie
        
        Args:
            api_key: DailyNutri API key
        """
        self.client = DailyNutriAPIClient(api_key)
        self.commands = {
            '/log': self.handle_log,
            '/query': self.handle_query,
            '/today': self.handle_today,
            '/yesterday': self.handle_yesterday,
            '/calories': self.handle_calories,
            '/protein': self.handle_protein,
            '/help': self.handle_help
        }
    
    def handle_message(self, telegram_message: str) -> str:
        """
        Verwerk een Telegram bericht en retourneer response
        
        Args:
            telegram_message: Bericht van Telegram gebruiker
        
        Returns:
            Response tekst voor Telegram
        """
        if not telegram_message or not telegram_message.strip():
            return "❌ Leeg bericht. Stuur iets als: 'Ik heb een appel gegeten' of '/help' voor commands."
        
        message = telegram_message.strip()
        
        # Check voor commands
        if message.startswith('/'):
            parts = message.split(' ', 1)
            command = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""
            
            if command in self.commands:
                return self.commands[command](args)
            else:
                return self.handle_unknown_command(command)
        
        # Geen command = probeer als food log
        return self.handle_log(message)
    
    def handle_log(self, food_description: str) -> str:
        """Verwerk food logging"""
        if not food_description:
            return "❌ Geef een beschrijving van wat je gegeten hebt. Bijv: 'Ik heb een broodje kaas gegeten'"
        
        try:
            result = self.client.log_food(food_description)
            
            if result.get('action') == 'logged':
                reply = result.get('reply', '✅ Genoteerd!')
                
                # Voeg item details toe indien beschikbaar
                if 'items' in result and result['items']:
                    items_text = "\n\n📋 Details:"
                    for item in result['items']:
                        name = item.get('item_name', 'Onbekend')
                        cals = item.get('calories', 0)
                        protein = item.get('protein', 0)
                        items_text += f"\n• {name}: {cals} kcal, {protein}g eiwit"
                    reply += items_text
                
                return reply
            else:
                return f"⚠️ {result.get('reply', 'Onverwachte response')}"
                
        except ValueError as e:
            return f"❌ Fout: {str(e)}"
        except Exception as e:
            return f"❌ Onverwachte fout: {str(e)}"
    
    def handle_query(self, question: str) -> str:
        """Verwerk voedingsquery"""
        if not question:
            return "❌ Stel een vraag over je voeding. Bijv: 'Wat heb ik gisteren gegeten?'"
        
        try:
            result = self.client.query_food_history(question)
            return result.get('reply', '⚠️ Geen antwoord ontvangen')
        except ValueError as e:
            return f"❌ Fout: {str(e)}"
        except Exception as e:
            return f"❌ Onverwachte fout: {str(e)}"
    
    def handle_today(self, args: str = "") -> str:
        """Samenvatting van vandaag"""
        try:
            result = self.client.get_today_summary()
            return result.get('reply', '⚠️ Geen data voor vandaag')
        except Exception as e:
            return f"❌ Fout: {str(e)}"
    
    def handle_yesterday(self, args: str = "") -> str:
        """Wat gisteren gegeten"""
        try:
            result = self.client.get_yesterday_food()
            return result.get('reply', '⚠️ Geen data voor gisteren')
        except Exception as e:
            return f"❌ Fout: {str(e)}"
    
    def handle_calories(self, args: str = "") -> str:
        """Calorieën vandaag"""
        try:
            result = self.client.get_calories_today()
            return result.get('reply', '⚠️ Geen calorie data voor vandaag')
        except Exception as e:
            return f"❌ Fout: {str(e)}"
    
    def handle_protein(self, args: str = "") -> str:
        """Eiwit deze week"""
        try:
            result = self.client.get_protein_this_week()
            return result.get('reply', '⚠️ Geen eiwit data voor deze week')
        except Exception as e:
            return f"❌ Fout: {str(e)}"
    
    def handle_help(self, args: str = "") -> str:
        """Toon help"""
        help_text = """🍎 DailyNutri Telegram Commands:

📝 Food Loggen:
• Stuur gewoon een bericht: "Ik heb een appel gegeten"
• Of gebruik: /log <beschrijving>
  Bijv: /log 2 boterhammen met pindakaas

📊 Queries:
• /query <vraag> - Stel vraag over voeding
  Bijv: /query Wat heb ik gisteren gegeten?
• /today - Samenvatting van vandaag
• /yesterday - Wat gisteren gegeten
• /calories - Calorieën vandaag
• /protein - Eiwit deze week

ℹ️ Info:
• /help - Toon deze help
• Taal: API antwoordt in je Hapklik profieltaal
• Meerdere items: "2 eieren, toast en koffie"
• Specifiek: "150g kipfilet" ipv "kip"

Voorbeelden:
• "Net een banaan en koffie gehad"
• "Lunch: salade met kip en dressing"
• /query Hoeveel calorieën heb ik deze week gehad?
"""
        return help_text
    
    def handle_unknown_command(self, command: str) -> str:
        """Onbekend command"""
        return f"❌ Onbekend command: {command}\nGebruik /help voor beschikbare commands."


def process_telegram_message(message: str, api_key: str = None) -> str:
    """
    Eenvoudige functie om Telegram berichten te verwerken
    
    Args:
        message: Telegram bericht
        api_key: Optionele API key
    
    Returns:
        Response voor Telegram
    """
    bot = DailyNutriTelegramBot(api_key)
    return bot.handle_message(message)


if __name__ == "__main__":
    """Test de Telegram bot"""
    import sys
    
    def print_usage():
        print("Usage: python telegram_bot.py <message>")
        print("\nVoorbeeld:")
        print('  python telegram_bot.py "Ik heb een appel gegeten"')
        print('  python telegram_bot.py "/query Wat heb ik gisteren gegeten?"')
        print('  python telegram_bot.py "/help"')
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    message = ' '.join(sys.argv[1:])
    
    try:
        bot = DailyNutriTelegramBot()
        response = bot.handle_message(message)
        print("🤖 Bot Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)
    
    except Exception as e:
        print(f"❌ Fout: {e}")
        sys.exit(1)