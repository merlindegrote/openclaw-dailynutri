#!/usr/bin/env python3
"""
Test script for DailyNutri Integration Skill
Tests all major components of the skill
"""

import os
import sys
import json
from pathlib import Path

def test_skill_structure():
    """Test if skill has correct structure"""
    print("🧪 Testing skill structure...")
    
    required_files = [
        "SKILL.md",
        "requirements.txt",
        "scripts/api_client.py",
        "scripts/telegram_bot.py",
        "scripts/openclaw_integration.py",
        "scripts/setup.py"
    ]
    
    skill_dir = Path(__file__).parent.parent
    
    missing_files = []
    for file in required_files:
        file_path = skill_dir / file
        if not file_path.exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ Skill structure is correct")
        return True

def test_python_dependencies():
    """Test Python dependencies"""
    print("\n🧪 Testing Python dependencies...")
    
    try:
        import requests
        print("✅ requests module is available")
        return True
    except ImportError:
        print("❌ requests module not found")
        print("Install with: pip install requests")
        return False

def test_api_client_structure():
    """Test API client structure"""
    print("\n🧪 Testing API client structure...")
    
    try:
        # Import the module to check syntax
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "api_client", 
            Path(__file__).parent / "api_client.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check if class exists
        if hasattr(module, 'DailyNutriAPIClient'):
            print("✅ DailyNutriAPIClient class found")
            
            # Check required methods
            client = module.DailyNutriAPIClient(api_key="test_key")
            required_methods = ['log_food', 'query_food_history', 'send_message']
            
            for method in required_methods:
                if hasattr(client, method):
                    print(f"✅ Method '{method}' found")
                else:
                    print(f"❌ Method '{method}' not found")
                    return False
            
            return True
        else:
            print("❌ DailyNutriAPIClient class not found")
            return False
            
    except Exception as e:
        print(f"❌ Error testing API client: {e}")
        return False

def test_telegram_bot_structure():
    """Test Telegram bot structure"""
    print("\n🧪 Testing Telegram bot structure...")
    
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "telegram_bot", 
            Path(__file__).parent / "telegram_bot.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check if class exists
        if hasattr(module, 'DailyNutriTelegramBot'):
            print("✅ DailyNutriTelegramBot class found")
            
            # Check required methods
            bot = module.DailyNutriTelegramBot(api_key="test_key")
            required_methods = ['handle_message', 'handle_log', 'handle_query']
            
            for method in required_methods:
                if hasattr(bot, method):
                    print(f"✅ Method '{method}' found")
                else:
                    print(f"❌ Method '{method}' not found")
                    return False
            
            return True
        else:
            print("❌ DailyNutriTelegramBot class not found")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Telegram bot: {e}")
        return False

def test_openclaw_integration_structure():
    """Test OpenClaw integration structure"""
    print("\n🧪 Testing OpenClaw integration structure...")
    
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "openclaw_integration", 
            Path(__file__).parent / "openclaw_integration.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check if class exists
        if hasattr(module, 'OpenClawDailyNutriIntegration'):
            print("✅ OpenClawDailyNutriIntegration class found")
            
            # Check required methods
            integrator = module.OpenClawDailyNutriIntegration(api_key="test_key")
            required_methods = ['log_from_openclaw', 'query_from_openclaw', 'get_daily_summary']
            
            for method in required_methods:
                if hasattr(integrator, method):
                    print(f"✅ Method '{method}' found")
                else:
                    print(f"❌ Method '{method}' not found")
                    return False
            
            return True
        else:
            print("❌ OpenClawDailyNutriIntegration class not found")
            return False
            
    except Exception as e:
        print(f"❌ Error testing OpenClaw integration: {e}")
        return False

def test_setup_script():
    """Test setup script"""
    print("\n🧪 Testing setup script...")
    
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "setup", 
            Path(__file__).parent / "setup.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check if main function exists
        if hasattr(module, 'main'):
            print("✅ Setup script has main function")
            return True
        else:
            print("❌ Setup script missing main function")
            return False
            
    except Exception as e:
        print(f"❌ Error testing setup script: {e}")
        return False

def generate_test_report():
    """Generate test report"""
    print("\n" + "=" * 50)
    print("📊 DailyNutri Integration Skill Test Report")
    print("=" * 50)
    
    tests = [
        ("Skill Structure", test_skill_structure()),
        ("Python Dependencies", test_python_dependencies()),
        ("API Client", test_api_client_structure()),
        ("Telegram Bot", test_telegram_bot_structure()),
        ("OpenClaw Integration", test_openclaw_integration_structure()),
        ("Setup Script", test_setup_script())
    ]
    
    passed = sum(1 for _, result in tests if result)
    total = len(tests)
    
    print(f"\n📈 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Skill is ready for use.")
        print("\n🚀 Next steps:")
        print("1. Add API key to .env: DAILY_NUTRI_API_KEY=hk_your_key")
        print("2. Run setup: python3 scripts/setup.py")
        print("3. Test with: python3 scripts/api_client.py log 'test'")
        return True
    else:
        print("\n❌ Some tests failed. Please fix the issues above.")
        return False

def main():
    """Main test function"""
    print("🍎 DailyNutri Integration Skill Test Suite")
    print("=" * 50)
    
    success = generate_test_report()
    
    if success:
        print("\n✅ Skill is ready for GitHub and ClawHub!")
        print("\n📁 To publish to GitHub:")
        print("1. Create new repository on GitHub")
        print("2. Initialize git in skill directory")
        print("3. Add files: git add .")
        print("4. Commit: git commit -m 'Initial release'")
        print("5. Push: git push origin main")
        print("\n🔗 To publish to ClawHub:")
        print("1. Package skill: openclaw skills package dailynutri-integration")
        print("2. Submit to ClawHub: https://clawhub.com/submit")
        
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())