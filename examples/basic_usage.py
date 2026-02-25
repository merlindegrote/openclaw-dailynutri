#!/usr/bin/env python3
"""
Basic Usage Examples for DailyNutri Integration Skill
"""

import sys
import os

# Add parent directory to path to import scripts
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from api_client import DailyNutriAPIClient
from telegram_bot import process_telegram_message
from openclaw_integration import log_food_openclaw, query_food_openclaw

def example_basic_logging():
    """Example: Basic food logging"""
    print("🍎 Example 1: Basic Food Logging")
    print("-" * 40)
    
    try:
        client = DailyNutriAPIClient()
        
        # Log a simple meal
        result = client.log_food("I had an apple and a coffee")
        print(f"Response: {result.get('reply', 'No reply')}")
        
        # Log with more detail
        result = client.log_food("Lunch: chicken salad with olive oil dressing")
        print(f"Response: {result.get('reply', 'No reply')}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def example_nutrition_queries():
    """Example: Nutrition queries"""
    print("\n📊 Example 2: Nutrition Queries")
    print("-" * 40)
    
    try:
        client = DailyNutriAPIClient()
        
        # Ask about today's calories
        result = client.query_food_history("How many calories have I had today?")
        print(f"Calories today: {result.get('reply', 'No data')}")
        
        # Ask about yesterday's meals
        result = client.query_food_history("What did I eat yesterday?")
        print(f"Yesterday's meals: {result.get('reply', 'No data')}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def example_telegram_integration():
    """Example: Telegram bot integration"""
    print("\n🤖 Example 3: Telegram Bot Integration")
    print("-" * 40)
    
    # Simulate Telegram messages
    messages = [
        "I just had a banana",
        "/query What did I eat for breakfast today?",
        "Lunch: pasta with tomato sauce and a glass of water",
        "/help"
    ]
    
    for message in messages:
        print(f"\nUser: {message}")
        response = process_telegram_message(message)
        print(f"Bot: {response[:100]}...")

def example_openclaw_integration():
    """Example: OpenClaw workflow integration"""
    print("\n🔗 Example 4: OpenClaw Workflow Integration")
    print("-" * 40)
    
    try:
        # Log food with context
        result = log_food_openclaw(
            "Greek yogurt with honey and walnuts",
            context="breakfast"
        )
        
        print(f"Status: {result.get('status', 'unknown')}")
        print(f"Message: {result.get('message', 'No message')}")
        
        if result.get('status') == 'success':
            details = result.get('details', {})
            print(f"Items logged: {details.get('items_logged', 0)}")
            print(f"Total calories: {details.get('total_calories', 0)}")
        
        # Query nutrition
        result = query_food_openclaw("How much protein have I had this week?")
        print(f"\nQuery result: {result.get('reply', 'No data')}")
        
    except Exception as e:
        print(f"Error: {e}")

def example_error_handling():
    """Example: Error handling"""
    print("\n⚠️ Example 5: Error Handling")
    print("-" * 40)
    
    # Test with invalid API key
    print("Testing error scenarios...")
    
    try:
        # This would fail without proper API key
        client = DailyNutriAPIClient(api_key="invalid_key")
        result = client.log_food("test")
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Expected error caught: {e}")
    except Exception as e:
        print(f"Other error: {e}")

def main():
    """Run all examples"""
    print("🍎 DailyNutri Integration Skill - Usage Examples")
    print("=" * 60)
    
    print("\n⚠️ Note: These examples require a valid API key in your .env file")
    print("Add: DAILY_NUTRI_API_KEY=hk_your_api_key_here")
    print("=" * 60)
    
    example_basic_logging()
    example_nutrition_queries()
    example_telegram_integration()
    example_openclaw_integration()
    example_error_handling()
    
    print("\n" + "=" * 60)
    print("✅ Examples completed!")
    print("\nFor more examples, see SKILL.md documentation")

if __name__ == "__main__":
    main()