#! python3
import pyautogui
import time
from appIsOpenCheck import appIsOpenCheck
from lib import itemCosting
from lib import clearAppScreen

# Input from user
site = '370'
costSet = 'current'
item = "TEST"
freezeUnfreeze = 'u'
freightPercent = '2.5'
overheadPercent = '80'
changeStatusTo = 'AC1'
purchasedPart = False
purchasePrice = 0

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
pyautogui.hotkey('alt', ' ')
pyautogui.press('x')  
time.sleep(1)

clearAppScreen.clearAppScreen()
itemCosting.freezeAndUnfreeze(site, costSet, item, freezeUnfreeze)

itemCosting.costRollUp(site, costSet, item)

itemCosting.elementCostCalc(item, costSet, freightPercent)

itemCosting.overheadCostUpdate(item, costSet, overheadPercent)

itemCosting.productStructureCostRollUp(site, costSet, item)

itemCosting.itemDataMaint(item, changeStatusTo)

if costSet == 'standard':
    itemCosting.freezeAndUnfreeze(site, costSet, item, 'f')