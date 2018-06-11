import pyautogui

def clearAppScreen():
    # Clear any open menus
    pyautogui.hotkey('alt', 'w', 'l')
    pyautogui.press('esc')
    # Check for empty screen background
    while pyautogui.pixelMatchesColor(1500, 200, (194, 196, 197)) == False:
        print('#Check for empty screen: RGB not matched')
