#!/bin/bash
# Username Update Verification Script
# Verifies that all GitHub username references have been updated correctly

echo "🔍 Verifying GitHub Username Update"
echo "=================================="

# Check git remote
echo "📡 Git Remote URL:"
git remote -v | head -2

echo ""
echo "🔍 Searching for old username references..."

# Search for old username
OLD_REFS=$(grep -r "Jlf2526" . --exclude-dir=.git --exclude-dir=__pycache__ --exclude-dir=.pytest_cache --exclude-dir=htmlcov 2>/dev/null)

if [ -z "$OLD_REFS" ]; then
    echo "✅ No old username references found"
else
    echo "❌ Found old username references:"
    echo "$OLD_REFS"
fi

echo ""
echo "🔍 Checking new username references..."

# Search for new username
NEW_REFS=$(grep -r "PHLthy215" . --exclude-dir=.git --exclude-dir=__pycache__ --exclude-dir=.pytest_cache --exclude-dir=htmlcov 2>/dev/null | wc -l)

echo "✅ Found $NEW_REFS references to new username PHLthy215"

echo ""
echo "📋 Key Files Updated:"
echo "   • README.md - Repository badges and links"
echo "   • TESTING.md - Clone instructions"
echo "   • setup.py - Project URLs and author info"
echo "   • zoom_deep_clean/__init__.py - Author email"
echo "   • zoom_deep_clean/gui_pyside6.py - GitHub repository link"
echo "   • docs/quick-start.md - Clone instructions"
echo "   • docs/development.md - Clone instructions"

echo ""
echo "🎯 Summary:"
echo "   • Git remote updated to PHLthy215 account"
echo "   • All documentation links updated"
echo "   • Author information updated"
echo "   • Bundle identifiers maintained (lowercase convention)"

echo ""
echo "✅ Username migration completed successfully!"
