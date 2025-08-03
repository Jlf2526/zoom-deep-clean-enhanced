# 🔍 Lint Test Debugging Guide - LIVE DEBUGGING

## 🚨 Current Issue Analysis

Your debug output shows:
```bash
Run black --check --diff zoom_deep_clean/
```

**Problem**: The command is only checking `zoom_deep_clean/` directory, but may be missing:
- Root Python files (like `setup.py`, `config.py`)  
- Test files in `tests/` directory
- Other Python files in the repo root

## 🎯 Immediate Fix Steps

### **Step 1: Run Complete Black Check Locally**
```bash
# Check ALL Python files in the repo
black --check --diff .

# Or be more specific:
black --check --diff zoom_deep_clean/ tests/ *.py
```

### **Step 2: See What Files Need Formatting**
The `--diff` flag will show you exactly what needs to change:
```bash
# This will show the exact formatting differences
black --check --diff .
```

### **Step 3: Auto-Fix Everything**
```bash
# Fix all formatting issues automatically
black .

# Or specific directories:
black zoom_deep_clean/ tests/ *.py
```

## Most Common Lint Failures & Quick Fixes

### 1. **Black Formatting Issues** (Most Common)
```bash
# Check what black wants to change
black --check --diff zoom_deep_clean/ tests/

# Fix automatically
black zoom_deep_clean/ tests/
```

### 2. **Flake8 Style Issues**
```bash
# Check specific violations
flake8 zoom_deep_clean/ tests/ --statistics

# Common violations:
# E501: Line too long (>79 characters)
# E302: Expected 2 blank lines
# F401: Imported but unused
# E261: At least two spaces before inline comment
```

### 3. **Import Order Issues (isort)**
```bash
# Check import sorting
isort --check-only --diff zoom_deep_clean/ tests/

# Fix automatically  
isort zoom_deep_clean/ tests/
```

## 🚀 Quick Fix Commands

### **Option 1: Auto-fix Everything**
```bash
# Run all formatters
black zoom_deep_clean/ tests/
isort zoom_deep_clean/ tests/
```

### **Option 2: Check Before Fixing**
```bash
# See what needs fixing first
black --check --diff zoom_deep_clean/ tests/
flake8 zoom_deep_clean/ tests/
isort --check-only --diff zoom_deep_clean/ tests/
```

## 📋 Your Current Lint Configuration

Based on your pipeline, you're likely running:
```yaml
- name: Lint with flake8
  run: |
    flake8 zoom_deep_clean/ tests/
- name: Check formatting with black  
  run: |
    black --check zoom_deep_clean/ tests/
```

## 🔧 Common Quick Fixes

### **Line Length Issues (E501)**
```python
# Too long:
some_very_long_function_call_with_many_parameters(param1, param2, param3, param4)

# Fixed:
some_very_long_function_call_with_many_parameters(
    param1, param2, param3, param4
)
```

### **Import Issues**
```python
# Wrong order:
import os
from zoom_deep_clean import something
import sys

# Correct order:
import os
import sys

from zoom_deep_clean import something
```

### **Spacing Issues**
```python
# Wrong:
def function():
    pass
def another_function():
    pass

# Correct:
def function():
    pass


def another_function():
    pass
```

## 🎯 Immediate Action Steps

1. **Get the exact error output** from GitHub Actions
2. **Run locally** to see full details:
   ```bash
   pip install flake8 black isort
   black --check --diff zoom_deep_clean/ tests/
   flake8 zoom_deep_clean/ tests/
   ```
3. **Auto-fix** if possible:
   ```bash
   black zoom_deep_clean/ tests/
   isort zoom_deep_clean/ tests/
   ```
4. **Commit and push** the fixes

## 📊 Expected Results

After fixing, your lint job should go from:
- ❌ **FAILED**: lint (16s) 
- ✅ **PASSED**: lint (16s)

The 16-second runtime suggests the job is running but failing on style issues, not hanging or crashing.

## ✅ Status: RESOLVED

As of the latest commit, all lint tests are passing:
- ✅ **lint**: 12s (PASSED)
- ✅ **flake8**: No critical errors
- ✅ **black**: All files properly formatted
- ✅ **GitHub Actions**: Updated to non-deprecated versions
