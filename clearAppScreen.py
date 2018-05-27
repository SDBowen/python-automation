import pyautogui

def clearAppScreen():
    # Clear any open menus
    pyautogui.hotkey('alt', 'w', 'l')
    pyautogui.press('esc')
    # Check for empty screen
    while pyautogui.pixelMatchesColor(308, 84, (186, 188, 189)) == False:
        print('#Check for empty screen: RGB not matched')
