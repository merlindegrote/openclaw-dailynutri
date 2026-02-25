# Contributing to DailyNutri Integration Skill

Thank you for your interest in contributing to the DailyNutri Integration Skill! This document provides guidelines and instructions for contributing.

## 🎯 Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## 🚀 Getting Started

### 1. Fork the Repository
Fork the repository on GitHub to your own account.

### 2. Clone Your Fork
```bash
git clone https://github.com/your-username/openclaw-dailynutri.git
cd openclaw-dailynutri
```

### 3. Set Up Development Environment
```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose

### Testing
- Write tests for new features
- Ensure existing tests pass
- Test edge cases and error conditions

### Documentation
- Update SKILL.md for new features
- Add examples to README.md
- Document API changes

## 🏗️ Project Structure

```
dailynutri-integration/
├── SKILL.md              # Main skill documentation
├── README.md             # GitHub README
├── CONTRIBUTING.md       # This file
├── LICENSE               # MIT License
├── requirements.txt      # Python dependencies
├── scripts/              # Main skill scripts
│   ├── api_client.py     # API client
│   ├── telegram_bot.py   # Telegram integration
│   ├── openclaw_integration.py  # OpenClaw integration
│   ├── setup.py          # Setup script
│   └── test_skill.py     # Test suite
└── examples/             # Example usage
```

## 🧪 Testing

### Run Test Suite
```bash
cd scripts
python3 test_skill.py
```

### Test Coverage
Ensure your changes don't break existing functionality:
- API client methods
- Telegram bot integration
- OpenClaw integration
- Error handling

## 📦 Adding New Features

### 1. Feature Request
Before implementing a new feature:
1. Check if it already exists
2. Consider if it aligns with the skill's purpose
3. Discuss in GitHub Issues if unsure

### 2. Implementation Steps
1. Update the relevant script(s)
2. Add tests for the new feature
3. Update documentation
4. Test with real API (if applicable)

### 3. Common Feature Types
- **New API endpoints**: Add to `api_client.py`
- **New integrations**: Create new script in `scripts/`
- **UI improvements**: Update existing scripts
- **Bug fixes**: Fix in relevant script

## 🐛 Reporting Bugs

### Bug Report Template
```markdown
## Description
[Clear description of the bug]

## Steps to Reproduce
1. [First step]
2. [Second step]
3. [Expected vs actual behavior]

## Environment
- OpenClaw version: [version]
- Python version: [version]
- Operating System: [OS]

## Additional Context
[Any additional information]
```

## 🔄 Pull Request Process

### 1. Prepare Your Changes
```bash
# Run tests
python3 scripts/test_skill.py

# Check code style
python -m py_compile scripts/*.py

# Update documentation if needed
```

### 2. Create Pull Request
1. Push your branch to GitHub
2. Create a pull request to the main repository
3. Fill out the PR template

### 3. PR Review
- Address any review comments
- Update your branch if requested
- Ensure all tests pass

### 4. Merge
Once approved, a maintainer will merge your PR.

## 📚 Documentation Updates

### SKILL.md Updates
- Add new sections for new features
- Update API reference if methods change
- Add examples for new functionality

### README.md Updates
- Update installation instructions if needed
- Add new usage examples
- Update feature list

## 🔒 Security

### Security Guidelines
- Never commit API keys or secrets
- Use environment variables for sensitive data
- Validate all user input
- Handle API errors gracefully

### Reporting Security Issues
Please report security issues privately via GitHub Issues with the "security" label.

## 🏆 Recognition

Contributors will be:
- Listed in the README.md (optional)
- Acknowledged in release notes
- Thanked in the project

## ❓ Getting Help

- Check existing documentation in SKILL.md
- Look at existing issues on GitHub
- Ask in the OpenClaw Discord community

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the DailyNutri Integration Skill! 🎉