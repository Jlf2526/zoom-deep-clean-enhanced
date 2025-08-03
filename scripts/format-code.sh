#!/bin/bash
# Pre-commit code formatting script
# Run this before committing to ensure code passes CI formatting checks

set -e

echo "🎨 Running Black code formatter..."

# Activate virtual environment if it exists
if [ -d "test_env" ]; then
    source test_env/bin/activate
    echo "✅ Using virtual environment"
elif command -v black &> /dev/null; then
    echo "✅ Using system Black installation"
else
    echo "❌ Black not found. Please install it:"
    echo "   pip install black"
    exit 1
fi

# Check Black version
echo "📋 Black version: $(black --version)"

# Format all Python files
echo "🔧 Formatting Python files..."
black setup.py scripts/ tests/ zoom_deep_clean/

# Verify formatting
echo "✅ Verifying formatting..."
if black --check setup.py scripts/ tests/ zoom_deep_clean/; then
    echo "🎉 All files are properly formatted!"
    echo "💡 Ready to commit and push!"
else
    echo "❌ Some files still need formatting"
    exit 1
fi

echo ""
echo "📋 Next steps:"
echo "   git add -A"
echo "   git commit -m 'your commit message'"
echo "   git push origin main"
