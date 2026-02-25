#!/bin/bash
# DailyNutri Integration Skill - GitHub Preparation Script

echo "🚀 DailyNutri Integration Skill - GitHub Preparation"
echo "=================================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

# Check if we're in the skill directory
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ ! -f "$SKILL_DIR/SKILL.md" ]]; then
    echo "❌ Not in skill directory. Please run from skill root."
    exit 1
fi

echo "📁 Skill directory: $SKILL_DIR"

# Initialize git repository
if [[ ! -d "$SKILL_DIR/.git" ]]; then
    echo "🔧 Initializing git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Check git status
echo "\n📊 Git status:"
git status --short

# Create .gitignore
echo "\n📝 Creating .gitignore..."
cat > "$SKILL_DIR/.gitignore" << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
logs/
*.log

# Temporary files
*.tmp
*.temp

# API keys and secrets
*.key
*.pem
config.json
EOF
echo "✅ .gitignore created"

# Add all files
echo "\n📦 Adding files to git..."
git add .

# Check what will be committed
echo "\n📋 Files to be committed:"
git status --short

# Create initial commit
echo "\n💾 Creating initial commit..."
git commit -m "Initial release: DailyNutri Integration Skill v1.0.0

Features:
- Natural language food logging via DailyNutri API
- Nutrition history queries
- Telegram bot integration
- OpenClaw workflow integration
- Automated reporting and monitoring
- Comprehensive documentation

Author: Merlin AI Assistant
Date: $(date +%Y-%m-%d)
Version: 1.0.0"

echo "\n✅ Commit created!"

# Show repository info
echo "\n📊 Repository information:"
echo "Branch: $(git branch --show-current)"
echo "Commit: $(git log --oneline -1)"

# Instructions for GitHub
echo "\n🚀 Next steps to publish on GitHub:"
echo "1. Create a new repository on GitHub:"
echo "   https://github.com/new"
echo "2. Name it: openclaw-dailynutri"
echo "3. Description: OpenClaw skill for DailyNutri API integration"
echo "4. Choose: Public repository"
echo "5. DO NOT initialize with README, .gitignore, or license"
echo "6. Copy the remote URL"
echo "7. Run these commands:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/openclaw-dailynutri.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""

# Instructions for ClawHub
echo "🔗 To publish on ClawHub:"
echo "1. Package the skill:"
echo "   openclaw skills package dailynutri-integration"
echo "2. Submit to ClawHub:"
echo "   https://clawhub.com/submit"
echo "3. Fill in skill details:"
echo "   - Name: DailyNutri Integration"
echo "   - Description: Natural language food logging and nutrition tracking"
echo "   - Category: Health & Fitness"
echo "   - Tags: nutrition, food-logging, health, api"
echo ""

echo "🎉 Skill is ready for distribution!"
echo "=================================================="