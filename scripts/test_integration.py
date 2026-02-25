#!/usr/bin/env python3
"""
Test DailyNutri integratie zonder API key
Toont hoe het systeem werkt
"""

print("🍎 DailyNutri API Integratie Test")
print("=" * 50)

print("\n📋 Implementatie Voltooid:")
print("1. ✅ API Client - api_client.py")
print("2. ✅ Telegram Bot - telegram_bot.py")
print("3. ✅ OpenClaw Integratie - openclaw_integration.py")
print("4. ✅ Setup Script - setup.py")
print("5. ✅ Documentatie - README.md")

print("\n🔧 Wat je nodig hebt:")
print("1. DailyNutri API key (begint met hk_)")
print("2. Voeg toe aan .env: DAILY_NUTRI_API_KEY=hk_jouw_key_hier")
print("3. Run setup: python3 setup.py")

print("\n🚀 Gebruiksvoorbeelden:")

print("\n📝 Food Loggen:")
print('''
# Directe API call
python3 api_client.py log "Ik heb een broodje kaas gegeten"

# Met context
python3 openclaw_integration.py log "Yoghurt met granola" breakfast

# Via Telegram style
python3 telegram_bot.py "Net een appel en noten gehad"
''')

print("\n📊 Queries:")
print('''
# Vraag over voeding
python3 api_client.py query "Wat heb ik gisteren gegeten?"

# Calorieën vandaag
python3 api_client.py calories

# Eiwit deze week
python3 api_client.py protein

# Via Telegram command
python3 telegram_bot.py "/query Hoeveel calorieën heb ik vandaag gehad?"
''')

print("\n📈 Monitoring:")
print('''
# Log geschiedenis
python3 openclaw_integration.py history

# Wekelijks rapport
python3 openclaw_integration.py report

# Dagelijkse samenvatting
python3 openclaw_integration.py summary
''')

print("\n🔗 API Details:")
print("• Endpoint: https://relwosnejsszbqazxywz.supabase.co/functions/v1/api-gateway")
print("• Auth: X-API-Key header met hk_... key")
print("• Rate Limit: 60 requests per minuut")
print("• Taal: Volgt Hapklik profieltaal (NL/EN/FR/DE)")

print("\n💡 Tips voor beste resultaten:")
print("1. Wees specifiek: '150g kipfilet' ipv 'kip'")
print("2. Gebruik context: breakfast, lunch, dinner, snack")
print("3. Meerdere items: '2 eieren, toast en koffie'")
print("4. Log direct na eten voor accurate tracking")
print("5. Monitor rate limits bij veelvuldig gebruik")

print("\n📁 Bestanden aangemaakt:")
import os
for root, dirs, files in os.walk("/config/.openclaw/workspace/dailynutri"):
    level = root.replace("/config/.openclaw/workspace/dailynutri", "").count(os.sep)
    indent = " " * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = " " * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

print("\n🎯 Volgende Stappen:")
print("1. Voeg API key toe aan .env file")
print("2. Run: python3 setup.py")
print("3. Test met: python3 api_client.py log 'test'")
print("4. Integreer met OpenClaw workflows")
print("5. Setup cron jobs voor automatische samenvattingen")

print("\n✅ Implementatie klaar - wacht op API key!")
print("=" * 50)