# DailyNutri Integration Skill

## 🍎 Overview

The DailyNutri Integration Skill enables OpenClaw agents to interact with the DailyNutri (Hapklik) API for food logging and nutrition tracking using natural language. This skill provides a seamless interface for logging meals, querying nutrition history, and generating dietary reports.

## ✨ Features

- **Natural Language Food Logging**: Log meals using everyday language
- **Nutrition History Queries**: Ask questions about your dietary history
- **Telegram Bot Integration**: Log food via Telegram messages
- **OpenClaw Workflow Integration**: Seamless integration with existing workflows
- **Automated Reporting**: Generate daily/weekly nutrition summaries
- **Multi-language Support**: Follows your Hapklik profile language (NL/EN/FR/DE)

## 📋 Prerequisites

1. **DailyNutri Account**: Sign up at [dailynutri.app](https://dailynutri.app)
2. **API Key**: Create an API key in your Hapklik profile (Profile → API Keys)
3. **OpenClaw Installation**: Running OpenClaw with skill support

## 🔧 Installation

### Method 1: From ClawHub (Recommended)
```bash
openclaw skills install dailynutri-integration
```

### Method 2: Manual Installation
```bash
# Clone the repository
git clone https://github.com/[username]/openclaw-dailynutri.git
cd openclaw-dailynutri

# Copy to skills directory
cp -r dailynutri-integration ~/.openclaw/skills/
```

### Method 3: Direct Download
```bash
# Download and extract
curl -L https://github.com/[username]/openclaw-dailynutri/archive/main.tar.gz | tar -xz
mv openclaw-dailynutri-main/dailynutri-integration ~/.openclaw/skills/
```

## ⚙️ Configuration

### 1. Add API Key to Environment
Add your DailyNutri API key to your `.env` file:

```bash
DAILY_NUTRI_API_KEY=hk_your_api_key_here
```

### 2. Run Setup Script
```bash
cd ~/.openclaw/skills/dailynutri-integration/scripts
python3 setup.py
```

### 3. Verify Installation
```bash
python3 test_skill.py
```

## 🚀 Usage

### Basic Food Logging
```python
from scripts.api_client import DailyNutriAPIClient

client = DailyNutriAPIClient()
result = client.log_food("I had an apple and a coffee")
print(result['reply'])
```

### Nutrition Queries
```python
result = client.query_food_history("What did I eat yesterday?")
print(result['reply'])
```

### Telegram Bot Integration
```python
from scripts.telegram_bot import process_telegram_message

response = process_telegram_message("I just had lunch: salad with chicken")
print(response)
```

### OpenClaw Integration
```python
from scripts.openclaw_integration import log_food_openclaw

result = log_food_openclaw("Yogurt with granola", context="breakfast")
print(result['message'])
```

## 📖 API Reference

### DailyNutriAPIClient Class

#### `__init__(api_key=None)`
Initialize the API client. If no API key is provided, it will be read from the environment variable `DAILY_NUTRI_API_KEY`.

#### `log_food(food_description)`
Log food using natural language description.

**Parameters:**
- `food_description` (str): Description of what was eaten/drunk

**Returns:** Dict with API response

#### `query_food_history(question)`
Ask a question about nutrition history.

**Parameters:**
- `question` (str): Question about nutrition

**Returns:** Dict with API response

#### `get_today_summary()`
Get summary of today's nutrition.

**Returns:** Dict with today's summary

#### `get_yesterday_food()`
Get what was eaten yesterday.

**Returns:** Dict with yesterday's food

#### `get_calories_today()`
Get calories consumed today.

**Returns:** Dict with calorie information

#### `get_protein_this_week()`
Get protein consumed this week.

**Returns:** Dict with protein information

### Telegram Bot Functions

#### `process_telegram_message(message, api_key=None)`
Process a Telegram message and return appropriate response.

**Parameters:**
- `message` (str): Telegram message from user
- `api_key` (str, optional): API key

**Returns:** Response text for Telegram

### OpenClaw Integration Functions

#### `log_food_openclaw(food_description, context=None, api_key=None)`
Log food from OpenClaw with context.

**Parameters:**
- `food_description` (str): Food description
- `context` (str, optional): Context (breakfast, lunch, dinner, snack)
- `api_key` (str, optional): API key

**Returns:** Dict with result

#### `query_food_openclaw(question, api_key=None)`
Query food from OpenClaw.

**Parameters:**
- `question` (str): Question about nutrition
- `api_key` (str, optional): API key

**Returns:** Dict with result

#### `get_daily_summary_openclaw(api_key=None)`
Get daily nutrition summary.

**Parameters:**
- `api_key` (str, optional): API key

**Returns:** Dict with summary

## 📊 Examples

### Example 1: Simple Food Logging
```python
from scripts.api_client import DailyNutriAPIClient

client = DailyNutriAPIClient()
result = client.log_food("2 eggs with toast and coffee")
print(f"Logged: {result['reply']}")
```

### Example 2: Daily Summary
```python
from scripts.openclaw_integration import get_daily_summary_openclaw

summary = get_daily_summary_openclaw()
print(f"Today's nutrition: {summary['summary']}")
```

### Example 3: Telegram Bot Command
```python
from scripts.telegram_bot import process_telegram_message

# User sends: "I had a banana"
response = process_telegram_message("I had a banana")
print(response)  # "✅ Logged! I added a banana (105 kcal) to your logbook."
```

### Example 4: Contextual Logging
```python
from scripts.openclaw_integration import log_food_openclaw

# Log breakfast with context
result = log_food_openclaw("Oatmeal with berries", context="breakfast")
if result['status'] == 'success':
    print(f"Successfully logged breakfast: {result['message']}")
```

### Example 5: Nutrition Query
```python
from scripts.api_client import DailyNutriAPIClient

client = DailyNutriAPIClient()
result = client.query_food_history("How many calories did I have today?")
print(result['reply'])
```

## 🔄 Integration with OpenClaw Workflows

### 1. Heartbeat Integration
Add to your `HEARTBEAT.md`:
```markdown
### Daily Nutrition Check
- [ ] Check today's nutrition summary
- [ ] Log any unlogged meals
- [ ] Generate weekly nutrition report
```

### 2. Cron Job for Daily Summary
```bash
# Add to crontab
0 20 * * * cd /path/to/skill/scripts && python3 daily_summary.py
```

### 3. Telegram Bot Integration
```python
# In your Telegram bot handler
if message.startswith('/food'):
    food_desc = message[6:].strip()
    response = process_telegram_message(food_desc)
    send_telegram_message(response)
```

## 🎯 Use Cases

### 1. Personal Nutrition Tracking
- Log meals throughout the day
- Track calorie and macronutrient intake
- Monitor dietary patterns over time

### 2. Health & Fitness Integration
- Integrate with workout tracking
- Monitor protein intake for muscle building
- Track hydration levels

### 3. Meal Planning
- Log planned meals in advance
- Track adherence to meal plans
- Generate shopping lists based on logged meals

### 4. Dietary Compliance
- Monitor specific dietary restrictions
- Track allergen exposure
- Ensure nutritional balance

## ⚠️ Error Handling

### Common Errors and Solutions

#### 1. API Key Errors (401)
```python
try:
    result = client.log_food("test")
except ValueError as e:
    if "401" in str(e):
        print("Invalid API key. Please check your DAILY_NUTRI_API_KEY.")
```

#### 2. Rate Limit Errors (429)
```python
import time

try:
    result = client.log_food("test")
except ValueError as e:
    if "429" in str(e):
        print("Rate limit reached. Waiting 60 seconds...")
        time.sleep(60)
```

#### 3. Server Errors (500)
```python
try:
    result = client.log_food("test")
except ValueError as e:
    if "500" in str(e):
        print("Server error. Please try again later.")
```

## 📈 Monitoring and Logging

### Log Files
- `logs/food_log.json`: All food logging attempts
- `logs/errors.log`: Error logs
- `logs/api_calls.log`: API call history

### View Logs
```bash
# View recent logs
python3 scripts/openclaw_integration.py history

# Generate weekly report
python3 scripts/openclaw_integration.py report
```

## 🔒 Security

### API Key Security
- Never commit API keys to version control
- Use environment variables for API keys
- Rotate API keys regularly

### Data Privacy
- Food logs are stored locally only
- No personal data is shared with third parties
- All API calls are encrypted (HTTPS)

## 🚀 Advanced Features

### 1. Batch Logging
```python
from scripts.batch_logger import BatchLogger

logger = BatchLogger()
meals = [
    ("Oatmeal with berries", "breakfast"),
    ("Chicken salad", "lunch"),
    ("Salmon with vegetables", "dinner")
]
results = logger.log_batch(meals)
```

### 2. Nutritional Analysis
```python
from scripts.nutrition_analyzer import NutritionAnalyzer

analyzer = NutritionAnalyzer()
analysis = analyzer.analyze_week()
print(f"Weekly average calories: {analysis['avg_calories']}")
```

### 3. Meal Pattern Detection
```python
from scripts.pattern_detector import PatternDetector

detector = PatternDetector()
patterns = detector.detect_patterns()
print(f"Most common breakfast: {patterns['common_breakfast']}")
```

## 🔧 Troubleshooting

### 1. Installation Issues
```bash
# Check Python dependencies
pip install -r requirements.txt

# Check skill directory
ls -la ~/.openclaw/skills/dailynutri-integration/
```

### 2. API Connection Issues
```bash
# Test API connection
python3 scripts/test_connection.py

# Check API key
echo $DAILY_NUTRI_API_KEY
```

### 3. Permission Issues
```bash
# Check file permissions
chmod +x scripts/*.py

# Check directory permissions
ls -la ~/.openclaw/skills/dailynutri-integration/
```

## 📚 Additional Resources

### Documentation
- [DailyNutri API Documentation](https://dailynutri.app/api-docs)
- [OpenClaw Skills Documentation](https://docs.openclaw.ai/skills)
- [GitHub Repository](https://github.com/[username]/openclaw-dailynutri)

### Support
- [GitHub Issues](https://github.com/[username]/openclaw-dailynutri/issues)
- [OpenClaw Discord](https://discord.com/invite/clawd)
- [DailyNutri Support](https://dailynutri.app/support)

## 📄 License

This skill is licensed under the MIT License. See the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please see the CONTRIBUTING.md file for guidelines.

## 🏆 Credits

- **DailyNutri API**: Provided by Hapklik
- **Skill Development**: Merlin AI Assistant
- **OpenClaw Integration**: OpenClaw Community

## 📊 Version History

### v1.0.0 (2026-02-25)
- Initial release
- Basic food logging and queries
- Telegram bot integration
- OpenClaw workflow integration
- Comprehensive documentation

---

**Skill ID**: `dailynutri-integration`  
**Version**: 1.0.0  
**Author**: Merlin AI Assistant  
**Last Updated**: 2026-02-25  
**OpenClaw Version**: 1.0.0+  
**Python Version**: 3.8+