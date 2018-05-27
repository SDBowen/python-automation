import pyautogui

def reportOutputCheck():
    # Report completion image
    runComplete = pyautogui.locateOnScreen('Capture.png', grayscale=True)
    # Check for menu run completion
    while runComplete == None:
        runComplete = pyautogui.locateOnScreen('Capture.png', grayscale=True)
        print('Waiting for report output...')
    print('Report run: Complete')
    pyautogui.hotkey('alt', 'w', 'l')