#! python3
import pyautogui
import time
from appIsOpenCheck import appIsOpenCheck
from clearAppScreen import clearAppScreen
from menuSelect import menuSelect
from reportOutputCheck import reportOutputCheck
from lib import itemCosting

# Input from user
menu = '13.12.1'
site = '370'
costSet = 'CURRENT'
item = "TEST"
freezeUnfreeze = 'u'

# Detect screen resolution
screenResolution = pyautogui.size()

# Determin if QAD application is open and add focus
appIsOpenCheck()

while True:
    window = pyautogui.getWindow(appIsOpenCheck())
    if window:
        window.set_foreground()
        break

# Maximize app
pyautogui.hotkey('alt', ' ', 'x')
time.sleep(2)

clearAppScreen()

menuSelect(menu)
    
itemCosting.freezeAndUnfreeze(site, costSet, item, freezeUnfreeze)

reportOutputCheck()
