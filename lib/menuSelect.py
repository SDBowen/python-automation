import pyautogui

def menuSelect(menu):
    # Select menu search
    pyautogui.hotkey('ctrl', 'm', 'delete')
    # Enter menu input from user
    pyautogui.typewrite(menu, .15)
    pyautogui.press('enter')
    if menu == '28.20.1.2':
        pyautogui.press('space')
    pyautogui.press('esc')
    # Check for screen change
    while pyautogui.pixelMatchesColor(1700, 200, (255, 255, 255)) == False:
        print('#Check for menu screen: RGB not matched')
    print('On menu screen...')