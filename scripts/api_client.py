#!/usr/bin/env python3
"""
DailyNutri (Hapklik) API Client
Voor food logging en voedingsgeschiedenis queries via natuurlijke taal
"""

import os
import json
import requests
from typing import Dict, List, Optional, Union
from datetime import datetime

class DailyNutriAPIClient:
    """Client voor DailyNutri Hapklik API Gateway"""
    
    def __init__(self, api_key: str = None):
        """
        Initializeer de API client
        
        Args:
            api_key: Hapklik API key (begint met hk_)
                    Als None, wordt geprobeerd uit .env te lezen
        """
        self.base_url = "https://relwosnejsszbqazxywz.supabase.co/functions/v1/api-gateway"
        
        if api_key:
            self.api_key = api_key
        else:
            # Probeer uit .env te lezen
            self.api_key = self._get_api_key_from_env()
        
        if not self.api_key:
            raise ValueError("API key is vereist. Voeg DAILY_NUTRI_API_KEY toe aan .env file of geef direct mee.")
        
        if not self.api_key.startswith('hk_'):
            print(f"⚠️  Waarschuwing: API key zou moeten beginnen met 'hk_' (huidige: {self.api_key[:10]}...)")
        
        self.headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }
    
    def _get_api_key_from_env(self) -> Optional[str]:
        """Haal API key uit .env file"""
        env_path = "/config/.openclaw/workspace/.env"
        
        try:
            with open(env_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('DAILY_NUTRI_API_KEY='):
                        return line.split('=', 1)[1].strip()
                    elif line.startswith('Dailynutri_API_KEY='):
                        return line.split('=', 1)[1].strip()
                    elif line.startswith('HAPKLIK_API_KEY='):
                        return line.split('=', 1)[1].strip()
        except FileNotFoundError:
            print(f"❌ .env file niet gevonden op {env_path}")
        except Exception as e:
            print(f"❌ Fout bij lezen .env: {e}")
        
        return None
    
    def send_message(self, message: str) -> Dict:
        """
        Stuur een bericht naar de API voor verwerking
        
        Args:
            message: Bericht in natuurlijke taal (max 1000 tekens)
                    Bijv: "Ik heb een broodje kaas gegeten"
                         of "Wat heb ik gisteren gegeten?"
        
        Returns:
            Dict met API response
            
        Raises:
            ValueError: Als message te lang is of leeg
            requests.exceptions.RequestException: Bij netwerk/API fouten
        """
        if not message or not message.strip():
            raise ValueError("Message mag niet leeg zijn")
        
        if len(message) > 1000:
            raise ValueError(f"Message te lang ({len(message)} tekens, max 1000)")
        
        data = {
            "message": message.strip()
        }
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=data,
                timeout=30  # 30 seconden timeout
            )
            
            # Handle verschillende status codes
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 400:
                raise ValueError(f"Ongeldig request: {response.text}")
            elif response.status_code == 401:
                raise ValueError("Ongeldige of verlopen API key")
            elif response.status_code == 402:
                raise ValueError("AI credits op - upgrade je account")
            elif response.status_code == 403:
                raise ValueError("Rol niet toegestaan (alleen unlimited/admin)")
            elif response.status_code == 429:
                retry_after = response.headers.get('Retry-After', 60)
                raise ValueError(f"Rate limit bereikt. Wacht {retry_after} seconden")
            elif response.status_code == 500:
                raise ValueError(f"Serverfout: {response.text}")
            else:
                raise ValueError(f"Onverwachte status {response.status_code}: {response.text}")
                
        except requests.exceptions.Timeout:
            raise ValueError("API timeout na 30 seconden")
        except requests.exceptions.ConnectionError:
            raise ValueError("Kon geen verbinding maken met API")
        except json.JSONDecodeError:
            raise ValueError(f"Ongeldige JSON response: {response.text}")
    
    def log_food(self, food_description: str) -> Dict:
        """
        Log food via natuurlijke taal beschrijving
        
        Args:
            food_description: Beschrijving van wat gegeten/gedronken is
                            Bijv: "2 boterhammen met pindakaas en een glas melk"
        
        Returns:
            Dict met logging resultaat
        """
        print(f"🍎 Food logging: {food_description}")
        return self.send_message(food_description)
    
    def query_food_history(self, question: str) -> Dict:
        """
        Stel een vraag over voedingsgeschiedenis
        
        Args:
            question: Vraag over voeding
                    Bijv: "Wat heb ik gisteren gegeten?"
                         "Hoeveel calorieën heb ik vandaag gehad?"
        
        Returns:
            Dict met query resultaat
        """
        print(f"📊 Query: {question}")
        return self.send_message(question)
    
    def get_today_summary(self) -> Dict:
        """Vraag samenvatting van voeding vandaag"""
        return self.query_food_history("Geef een samenvatting van mijn voeding van vandaag")
    
    def get_yesterday_food(self) -> Dict:
        """Vraag wat er gisteren gegeten is"""
        return self.query_food_history("Wat heb ik gisteren gegeten?")
    
    def get_calories_today(self) -> Dict:
        """Vraag hoeveel calorieën vandaag geconsumeerd"""
        return self.query_food_history("Hoeveel calorieën heb ik vandaag gehad?")
    
    def get_protein_this_week(self) -> Dict:
        """Vraag hoeveel eiwit deze week geconsumeerd"""
        return self.query_food_history("Hoeveel eiwit heb ik deze week gehad?")


# Helper functies voor eenvoudig gebruik
def log_food(message: str, api_key: str = None) -> Dict:
    """Eenvoudige functie om food te loggen"""
    client = DailyNutriAPIClient(api_key)
    return client.log_food(message)

def query_food(message: str, api_key: str = None) -> Dict:
    """Eenvoudige functie om query te stellen"""
    client = DailyNutriAPIClient(api_key)
    return client.query_food_history(message)


if __name__ == "__main__":
    """Test de API client"""
    import sys
    
    def print_usage():
        print("Usage: python api_client.py <command> <message>")
        print("Commands:")
        print("  log <food_description>    - Log food")
        print("  query <question>          - Stel vraag over voeding")
        print("  today                     - Samenvatting vandaag")
        print("  yesterday                 - Wat gisteren gegeten")
        print("  calories                  - Calorieën vandaag")
        print("  protein                   - Eiwit deze week")
        print("\nVoorbeeld:")
        print("  python api_client.py log 'Ik heb een appel gegeten'")
        print("  python api_client.py query 'Wat heb ik gisteren gegeten?'")
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    try:
        client = DailyNutriAPIClient()
        
        if command == "log" and len(sys.argv) >= 3:
            message = ' '.join(sys.argv[2:])
            result = client.log_food(message)
            print("✅ Success!")
            print(f"Action: {result.get('action', 'unknown')}")
            print(f"Reply: {result.get('reply', 'No reply')}")
            
            if 'items' in result:
                print(f"\n📋 Items logged:")
                for item in result['items']:
                    print(f"  • {item.get('item_name', 'Unknown')}: {item.get('calories', 0)} kcal")
        
        elif command == "query" and len(sys.argv) >= 3:
            message = ' '.join(sys.argv[2:])
            result = client.query_food_history(message)
            print("✅ Success!")
            print(f"Action: {result.get('action', 'unknown')}")
            print(f"Reply: {result.get('reply', 'No reply')}")
        
        elif command == "today":
            result = client.get_today_summary()
            print("✅ Vandaag samenvatting:")
            print(result.get('reply', 'Geen data'))
        
        elif command == "yesterday":
            result = client.get_yesterday_food()
            print("✅ Gisteren:")
            print(result.get('reply', 'Geen data'))
        
        elif command == "calories":
            result = client.get_calories_today()
            print("✅ Calorieën vandaag:")
            print(result.get('reply', 'Geen data'))
        
        elif command == "protein":
            result = client.get_protein_this_week()
            print("✅ Eiwit deze week:")
            print(result.get('reply', 'Geen data'))
        
        else:
            print_usage()
    
    except ValueError as e:
        print(f"❌ Fout: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Onverwachte fout: {e}")
        sys.exit(1)