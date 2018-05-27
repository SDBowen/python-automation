import pyautogui

def menuSelect(menu):
    # Select menu search
    pyautogui.hotkey('ctrl', 'm', 'delete')
    # Enter menu input from user
    pyautogui.typewrite(menu, .15)
    pyautogui.press('enter')
    pyautogui.press('esc')
    # Check for screen change
    while pyautogui.pixelMatchesColor(320, 160, (255, 255, 255)) == False:
        print('#Check for menu screen: RGB not matched')
    print('On menu screen...')