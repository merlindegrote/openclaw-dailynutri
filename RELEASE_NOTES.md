# DailyNutri Integration Skill - Release Notes

## v1.0.0 (2026-02-25)

### 🎉 Initial Release

**Core Features:**
- Natural language food logging via DailyNutri API
- Nutrition history queries and analysis
- Telegram bot integration for easy logging
- OpenClaw workflow integration
- Automated reporting and monitoring

### 🆕 New Features in v1.0.0

#### 1. Meal Name & Time Support
- **Automatic detection** of meal context from natural language
- **Meal names**: breakfast, lunch, dinner, snack, brunch
- **Meal times**: Support for "at 8:30 AM", "around noon", "for dinner"
- **Enhanced categorization**: Better organization of food logs

#### 2. Enhanced API Integration
- Improved error handling for meal_name and meal_time
- Better validation of meal time formats
- Graceful fallback when meal context cannot be determined

#### 3. Comprehensive Documentation
- Complete API reference with examples
- Integration guides for Telegram and OpenClaw
- Troubleshooting guide
- Backward compatibility notes

### 📦 Installation Methods

#### From GitHub:
```bash
git clone https://github.com/merlindegrote/openclaw-dailynutri.git
cd openclaw-dailynutri
cp -r dailynutri-integration ~/.openclaw/skills/
```

#### Direct Download:
```bash
curl -L https://github.com/merlindegrote/openclaw-dailynutri/archive/main.tar.gz | tar -xz
mv openclaw-dailynutri-main/dailynutri-integration ~/.openclaw/skills/
```

### 🔧 Configuration

1. **Get API Key**: Create at [dailynutri.app](https://dailynutri.app) → Profile → API Keys
2. **Add to .env**: `DAILY_NUTRI_API_KEY=hk_your_key_here`
3. **Run Setup**: `python3 scripts/setup.py`
4. **Test**: `python3 scripts/test_skill.py`

### 🚀 Usage Examples

#### Basic Logging:
```python
from scripts.api_client import DailyNutriAPIClient
client = DailyNutriAPIClient()
result = client.log_food("I had an apple")
```

#### Advanced Logging with Meal Context:
```python
result = client.log_food("I had breakfast: oatmeal with berries at 8:30 AM")
```

#### Nutrition Queries:
```python
result = client.query_food_history("What did I eat yesterday?")
```

### 🔄 Backward Compatibility

- **Old format**: `"I had an apple"` - still works
- **New format**: `"I had breakfast: oatmeal at 8 AM"` - recommended
- **Automatic detection**: Meal context extracted from natural language

### 🐛 Bug Fixes & Improvements

- Fixed API key validation
- Improved error messages
- Better timeout handling
- Enhanced logging capabilities

### 📚 Documentation Updates

- Complete API reference
- Integration examples
- Troubleshooting guide
- Meal context documentation
- Backward compatibility notes

### 🔗 Links

- **GitHub Repository**: https://github.com/merlindegrote/openclaw-dailynutri
- **DailyNutri API**: https://dailynutri.app/api-docs
- **OpenClaw Docs**: https://docs.openclaw.ai/skills
- **ClawHub**: https://clawhub.com

### 🏆 Credits

- **DailyNutri API**: Provided by Hapklik
- **Skill Development**: Merlin AI Assistant
- **OpenClaw Integration**: OpenClaw Community
- **Testing & Validation**: Peter (User)

### 📊 Technical Details

- **Skill ID**: `dailynutri-integration`
- **Version**: 1.0.0
- **Python**: 3.8+
- **OpenClaw**: 1.0.0+
- **License**: MIT
- **Author**: Merlin AI Assistant

---

**Ready for ClawHub Submission!** 🎯