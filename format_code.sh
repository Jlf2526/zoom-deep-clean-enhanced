#!/bin/bash
# Code Formatting Script
# Formats all Python files using black to meet CI/CD requirements

echo "🎨 Formatting Python code with black..."
echo "======================================"

# Check if black is installed
if ! command -v black &> /dev/null; then
    echo "❌ Black is not installed. Installing with pipx..."
    if ! command -v pipx &> /dev/null; then
        echo "Installing pipx first..."
        brew install pipx
    fi
    pipx install black
fi

# Navigate to project directory
cd "$(dirname "$0")"

echo "📁 Current directory: $(pwd)"
echo ""

# Run black formatter
echo "🔧 Running black formatter..."
black .

# Check the exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Code formatting completed successfully!"
    echo ""
    echo "📋 Next steps:"
    echo "   1. Review the changes: git diff"
    echo "   2. Add changes: git add ."
    echo "   3. Commit: git commit -m 'style: Format code with black'"
    echo "   4. Push: git push"
else
    echo ""
    echo "❌ Code formatting encountered issues."
    echo "   Please check the output above for details."
fi

echo ""
echo "💡 Tip: Run this script before committing to avoid CI formatting failures."
