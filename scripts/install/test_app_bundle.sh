#!/bin/bash

# Test the app bundle and show any errors

echo "🧪 Testing app bundle..."

APP_PATH="/Users/user/Documents/zoom-deep-clean-enhanced/Zoom Deep Clean Enhanced.app"
EXECUTABLE="$APP_PATH/Contents/MacOS/Zoom Deep Clean Enhanced"

echo "1. Checking app bundle structure..."
if [[ -d "$APP_PATH" ]]; then
    echo "✅ App bundle exists"
else
    echo "❌ App bundle not found"
    exit 1
fi

echo "2. Checking executable..."
if [[ -x "$EXECUTABLE" ]]; then
    echo "✅ Executable exists and is executable"
else
    echo "❌ Executable not found or not executable"
    exit 1
fi

echo "3. Testing executable directly..."
echo "Running: $EXECUTABLE"
echo "Output:"
"$EXECUTABLE" 2>&1 &
EXEC_PID=$!

# Wait a bit and check if process is still running
sleep 3
if kill -0 $EXEC_PID 2>/dev/null; then
    echo "✅ Process is running (PID: $EXEC_PID)"
    echo "Killing test process..."
    kill $EXEC_PID 2>/dev/null
else
    echo "❌ Process exited or failed to start"
fi

echo "4. Testing with 'open' command..."
open "$APP_PATH" 2>&1 &
sleep 2
echo "✅ 'open' command executed"

echo "5. Checking for Python/tkinter issues..."
cd "$APP_PATH/Contents/Resources"
python3 -c "
import tkinter as tk
try:
    root = tk.Tk()
    root.title('Test')
    root.geometry('200x100')
    root.after(1000, root.destroy)  # Auto-close after 1 second
    print('✅ tkinter window test passed')
    root.mainloop()
except Exception as e:
    print(f'❌ tkinter error: {e}')
"

echo "🎉 App bundle test completed!"
