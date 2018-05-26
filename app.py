#! python3
import pyautogui
import time
import ctypes
from appCheck import *

# Report completion image
runComplete = pyautogui.locateOnScreen('Capture.png', grayscale=True)

# Determin if QAD application is open
appIsOpenCheck()

# Detect screen resolution
screenResolution = pyautogui.size()

# Delay start
time.sleep(5)
#pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Detect if program is open
while True:
    #    window = pyautogui.getWindow('testdb: WATSUS Watson US [USD] > 370 Watson and Chalin US - QAD Enterprise Applications')
    window = pyautogui.getWindow(appIsOpenCheck())
    if window:
        window.set_foreground()
        break

# Focus on program and maximize
pyautogui.hotkey('alt', ' ', 'x')
time.sleep(2)

# Select menu search
pyautogui.hotkey('ctrl', 'm', 'delete')
# Select menu
pyautogui.typewrite('13.12.1', .25)
pyautogui.press('enter')

# Fill out menu
# Site
pyautogui.typewrite('370')
pyautogui.press('enter')
# Cost Set
pyautogui.typewrite('CURRENT')
pyautogui.press('enter')
# Item (From: and To:)
pyautogui.typewrite('TEST')
pyautogui.press('tab')
pyautogui.typewrite('TEST')
# Tab to next input field
for _ in range(11):
    pyautogui.press('tab')
# Freeze or Unfreeze
pyautogui.press('u')
pyautogui.press('enter')
# Submit form
pyautogui.press('enter')
# Check for menu run completion
while runComplete == None:
    runComplete = pyautogui.locateOnScreen('Capture.png', grayscale=True)
    print('searching')

print(runComplete)
