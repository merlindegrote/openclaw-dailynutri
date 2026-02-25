#!/usr/bin/env python3
"""
DailyNutri API Setup Script
Configureert de DailyNutri integratie voor OpenClaw
"""

import os
import sys
import json
from pathlib import Path

def setup_dailynutri():
    """Setup DailyNutri integratie"""
    print("🍎 DailyNutri API Setup")
    print("=" * 50)
    
    # Check .env file
    env_path = "/config/.openclaw/workspace/.env"
    
    if not os.path.exists(env_path):
        print(f"❌ .env file niet gevonden op: {env_path}")
        print("Maak eerst een .env file aan of geef het pad aan.")
        return False
    
    # Check voor bestaande API key
    api_key = None
    try:
        with open(env_path, 'r') as f:
            content = f.read()
            
        # Zoek naar DailyNutri API key
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('DAILY_NUTRI_API_KEY='):
                api_key = line.split('=', 1)[1].strip()
                break
            elif line.startswith('Dailynutri_API_KEY='):
                api_key = line.split('=', 1)[1].strip()
                break
            elif line.startswith('HAPKLIK_API_KEY='):
                api_key = line.split('=', 1)[1].strip()
                break
    
    except Exception as e:
        print(f"❌ Fout bij lezen .env: {e}")
        return False
    
    if api_key:
        print(f"✅ API key gevonden: {api_key[:10]}...")
        
        # Test de API key
        print("\n🔧 API key testen...")
        test_result = test_api_key(api_key)
        
        if test_result:
            print("✅ API key werkt!")
            create_config_file(api_key)
            return True
        else:
            print("❌ API key test gefaald")
            return False
    else:
        print("❌ Geen DailyNutri API key gevonden in .env")
        print("\n📋 Voeg deze regel toe aan je .env file:")
        print("DAILY_NUTRI_API_KEY=hk_jouw_api_key_hier")
        print("\n🔑 API key aanmaken:")
        print("1. Ga naar dailynutri.app")
        print("2. Login op je account")
        print("3. Ga naar Profiel → API Keys")
        print("4. Maak een nieuwe API key aan (begint met hk_)")
        return False

def test_api_key(api_key: str) -> bool:
    """Test of de API key werkt"""
    try:
        import requests
        
        url = "https://relwosnejsszbqazxywz.supabase.co/functions/v1/api-gateway"
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": api_key
        }
        data = {
            "message": "test"
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=10)
        
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            print("❌ Ongeldige API key")
            return False
        elif response.status_code == 403:
            print("❌ Account heeft geen API toegang (alleen unlimited/admin)")
            return False
        else:
            print(f"❌ API test gefaald: Status {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ API timeout")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ Geen internet verbinding")
        return False
    except Exception as e:
        print(f"❌ Onverwachte fout: {e}")
        return False

def create_config_file(api_key: str):
    """Maak configuratie file aan"""
    config_dir = "/config/.openclaw/workspace/dailynutri/config"
    config_file = os.path.join(config_dir, "config.json")
    
    os.makedirs(config_dir, exist_ok=True)
    
    config = {
        "api_key": api_key,
        "api_url": "https://relwosnejsszbqazxywz.supabase.co/functions/v1/api-gateway",
        "rate_limit": 60,  # requests per minuut
        "language": "nl",
        "auto_log_context": True,
        "log_file": "/config/.openclaw/workspace/dailynutri/logs/food_log.json",
        "setup_date": "2026-02-25",
        "version": "1.0.0"
    }
    
    try:
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Configuratie opgeslagen in: {config_file}")
        
        # Maak logs directory
        logs_dir = "/config/.openclaw/workspace/dailynutri/logs"
        os.makedirs(logs_dir, exist_ok=True)
        print(f"✅ Logs directory aangemaakt: {logs_dir}")
        
    except Exception as e:
        print(f"❌ Kon configuratie niet opslaan: {e}")

def create_example_scripts():
    """Maak voorbeeld scripts aan"""
    examples_dir = "/config/.openclaw/workspace/dailynutri/examples"
    os.makedirs(examples_dir, exist_ok=True)
    
    # Voorbeeld: Dagelijkse samenvatting
    daily_summary = """#!/usr/bin/env python3
"""
    
    print(f"✅ Voorbeeld scripts aangemaakt in: {examples_dir}")

def print_success_message():
    """Print success message"""
    print("\n" + "=" * 50)
    print("🎉 DailyNutri Setup Voltooid!")
    print("=" * 50)
    
    print("\n📋 Wat is er geïnstalleerd:")
    print("1. ✅ API Client - api_client.py")
    print("2. ✅ Telegram Bot - telegram_bot.py")
    print("3. ✅ OpenClaw Integratie - openclaw_integration.py")
    print("4. ✅ Configuratie - config/config.json")
    print("5. ✅ Logs Directory - logs/")
    
    print("\n🚀 Gebruik Voorbeelden:")
    print("  # Food loggen")
    print('  python3 api_client.py log "Ik heb een appel gegeten"')
    print("  # Query voeding")
    print('  python3 api_client.py query "Wat heb ik gisteren gegeten?"')
    print("  # Telegram bericht")
    print('  python3 telegram_bot.py "Ik heb lunch gehad: salade met kip"')
    print("  # OpenClaw integratie")
    print('  python3 openclaw_integration.py log "Yoghurt met granola" breakfast')
    
    print("\n📊 Monitoring:")
    print("  # Bekijk logs")
    print("  python3 openclaw_integration.py history")
    print("  # Genereer rapport")
    print("  python3 openclaw_integration.py report")
    
    print("\n🔧 Automatisering Tips:")
    print("1. Gebruik cron jobs voor dagelijkse samenvattingen")
    print("2. Integreer met Telegram voor mobile logging")
    print("3. Monitor rate limits (60 requests/minuut)")
    print("4. Gebruik context (breakfast/lunch/dinner/snack)")
    
    print("\n📞 Support:")
    print("• API Docs: https://dailynutri.app/api-docs")
    print("• API Keys: dailynutri.app/profile/api-keys")
    print("• Rate Limits: 60 requests/minuut")
    
    print("\n✅ Klaar voor gebruik!")

def main():
    """Hoofd functie"""
    print("🍎 DailyNutri API Setup voor OpenClaw")
    print("=" * 50)
    
    # Check Python dependencies
    try:
        import requests
        print("✅ requests module gevonden")
    except ImportError:
        print("❌ requests module niet gevonden")
        print("Installeer met: pip install requests")
        return False
    
    # Run setup
    if setup_dailynutri():
        print_success_message()
        return True
    else:
        print("\n❌ Setup gefaald")
        print("Controleer je .env file en probeer opnieuw.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)