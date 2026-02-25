# OpenClaw DailyNutri Integration Skill

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://clawhub.com)
[![Python Version](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive OpenClaw skill for integrating with the DailyNutri (Hapklik) API to enable natural language food logging and nutrition tracking.

## 🍎 Features

- **Natural Language Food Logging**: Log meals using everyday language
- **Nutrition History Queries**: Ask questions about your dietary history
- **Telegram Bot Integration**: Log food via Telegram messages
- **OpenClaw Workflow Integration**: Seamless integration with existing workflows
- **Automated Reporting**: Generate daily/weekly nutrition summaries
- **Multi-language Support**: Follows your Hapklik profile language (NL/EN/FR/DE)

## 📦 Installation

### From ClawHub (Recommended)
```bash
openclaw skills install dailynutri-integration
```

### Manual Installation
```bash
# Clone the repository
git clone https://github.com/merlindegrote/openclaw-dailynutri.git
cd openclaw-dailynutri

# Copy to skills directory
cp -r dailynutri-integration ~/.openclaw/skills/
```

### Direct Download
```bash
# Download and extract
curl -L https://github.com/merlindegrote/openclaw-dailynutri/archive/main.tar.gz | tar -xz
mv openclaw-dailynutri-main/dailynutri-integration ~/.openclaw/skills/
```

## ⚙️ Quick Start

1. **Get API Key**: Create one at [dailynutri.app](https://dailynutri.app) → Profile → API Keys
2. **Configure**: Add to your `.env` file:
   ```bash
   DAILY_NUTRI_API_KEY=hk_your_api_key_here
   ```
3. **Setup**: Run the setup script:
   ```bash
   cd ~/.openclaw/skills/dailynutri-integration/scripts
   python3 setup.py
   ```
4. **Test**: Verify installation:
   ```bash
   python3 test_skill.py
   ```

## 🚀 Usage Examples

### Basic Food Logging
```python
from scripts.api_client import DailyNutriAPIClient

client = DailyNutriAPIClient()
result = client.log_food("I had an apple and a coffee")
print(result['reply'])  # "✅ Logged! I added an apple (95 kcal)..."
```

### Advanced Food Logging with Meal Context
```python
from scripts.api_client import DailyNutriAPIClient

client = DailyNutriAPIClient()
# Specify meal name and time for better categorization
result = client.log_food("I had breakfast: oatmeal with berries at 8:30 AM")
print(result['reply'])  # "✅ Logged breakfast! I added oatmeal with berries..."
```

### Nutrition Queries
```python
result = client.query_food_history("What did I eat yesterday?")
print(result['reply'])  # "Yesterday you ate: ..."
```

### Telegram Integration
```python
from scripts.telegram_bot import process_telegram_message

response = process_telegram_message("I just had lunch: salad with chicken")
print(response)  # "✅ Logged! I added salad with chicken..."
```

## 🆕 New Features (v1.0.0)

### Meal Name & Time Support
The skill now supports enhanced meal logging with `meal_name` and `meal_time` context:

**Natural Language Integration:**
- **Meal Names**: breakfast, lunch, dinner, snack, brunch, etc.
- **Meal Times**: "at 8:30 AM", "around noon", "for dinner"
- **Automatic Detection**: The API automatically detects meal context from natural language

**Examples:**
```python
# Meal name and time in natural language
client.log_food("I had breakfast: oatmeal with berries at 8:30 AM")
client.log_food("Lunch was a chicken salad around 1 PM")
client.log_food("For dinner I had salmon with vegetables")
```

**Backward Compatibility:**
- Old format still works: "I had an apple"
- New format enhances categorization: "I had breakfast: oatmeal at 8 AM"

### Enhanced Error Handling
- Better validation for meal_name and meal_time parameters
- Graceful fallback when meal context cannot be determined
- Clear error messages for invalid meal times

## 📖 Documentation

Full documentation is available in [SKILL.md](SKILL.md), including:
- Complete API reference
- Integration examples
- Troubleshooting guide
- Advanced features

## 🔧 Requirements

- Python 3.8+
- OpenClaw 1.0.0+
- DailyNutri account with API access
- `requests` library

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Credits

- **DailyNutri API**: Provided by Hapklik
- **Skill Development**: Merlin AI Assistant
- **OpenClaw Integration**: OpenClaw Community

## 🔗 Links

- [DailyNutri Website](https://dailynutri.app)
- [OpenClaw Documentation](https://docs.openclaw.ai)
- [ClawHub](https://clawhub.com)
- [GitHub Repository](https://github.com/merlindegrote/openclaw-dailynutri)

---

**Skill ID**: `dailynutri-integration`  
**Version**: 1.0.0  
**Author**: Merlin AI Assistant  
**Last Updated**: 2026-02-25