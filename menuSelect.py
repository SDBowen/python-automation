import pyautogui

def menuSelect(menu):
    # Select menu search
    pyautogui.hotkey('ctrl', 'm', 'delete')
    # Enter menu input from user
    pyautogui.typewrite(menu, .25)
    pyautogui.press('enter')
    pyautogui.press('esc')
    # Check for screen change
    while pyautogui.pixelMatchesColor(320, 160, (255, 255, 255)) == False:
        print('#Check for report screen: RGB not matched')