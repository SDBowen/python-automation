import pyautogui, time
from .menuSelect import menuSelect
from .appScreenCheck import appScreenCheck
from .clearAppScreen import clearAppScreen

def freezeAndUnfreeze(site, costSet, item, status):
    menuSelect('13.12.1')
    appScreenCheck('freezeUnfreeze')    
    # Site
    pyautogui.typewrite(site)
    pyautogui.press('enter')
    # Cost Set
    pyautogui.typewrite(costSet)
    pyautogui.press('enter')
    # Item (From: and To:)
    pyautogui.typewrite(item)
    pyautogui.press('tab')
    pyautogui.typewrite(item)
    # Tab to next input field
    for _ in range(11):
        pyautogui.press('tab')
    # Freeze or Unfreeze
    pyautogui.press(status)
    pyautogui.press('enter')
    # Submit form
    pyautogui.press('enter')
    print('freezeUnfreeze Completed')
    appScreenCheck('report')
    clearAppScreen()

def costRollUp(site, costSet, item):
    menuSelect('14.13.13')
    appScreenCheck('routing')
    # Site
    pyautogui.typewrite(site)
    pyautogui.press('enter')
    # Cost Set
    pyautogui.typewrite(costSet)
    pyautogui.press('enter')
    # Item (From: and To:)
    pyautogui.typewrite(item)
    pyautogui.press('tab')
    pyautogui.typewrite(item)
    for _ in range(2):
        pyautogui.press('enter')
    print('costRollUp Completed')
    appScreenCheck('report')
    clearAppScreen()

def elementCostCalc(item, costSet, freightPercent):
    menuSelect('30.17.10')
    appScreenCheck('element')
    for _ in range(2):
        pyautogui.press('tab')
    # Item (From: and To:)    
    pyautogui.typewrite(item)
    pyautogui.press('tab')
    pyautogui.typewrite(item)
    for _ in range(5):
        pyautogui.press('tab')
    # Cost Set
    pyautogui.typewrite(costSet)
    pyautogui.press('tab')
    # Cost element
    pyautogui.typewrite('FREIGHT')
    pyautogui.press('tab')
    pyautogui.typewrite('MATERIAL')
    pyautogui.press('tab')
    pyautogui.typewrite(freightPercent)
    pyautogui.press('tab')
    pyautogui.typewrite('SUBCONTR')
    pyautogui.press('tab')
    pyautogui.typewrite(freightPercent)
    for _ in range(29):
        pyautogui.press('tab')
    pyautogui.press('space')
    for _ in range(2):
        pyautogui.press('enter')
    print('elementCostCalc Completed')
    appScreenCheck('report')
    clearAppScreen()

def overheadCostUpdate(item, costSet, overheadPercent):
    menuSelect('1.4.21')
    appScreenCheck('overhead')
    for _ in range(2):
        pyautogui.press('tab')
    # Item (From: and To:)
    pyautogui.typewrite(item)
    pyautogui.press('tab')
    pyautogui.typewrite(item)
    for _ in range(5):
        pyautogui.press('tab')
    # Cost Set
    pyautogui.typewrite(costSet)
    for _ in range(3):
        pyautogui.press('tab')
    pyautogui.typewrite(overheadPercent)
    for _ in range(2):
        pyautogui.press('tab')
    pyautogui.typewrite('0')
    for _ in range(4):
        pyautogui.press('tab')
    pyautogui.press('space')
    for _ in range(2):
        pyautogui.press('enter')
    print('overheadCostUpdate Completed')
    appScreenCheck('report')
    clearAppScreen()

def productStructureCostRollUp(site, costSet, item):
    menuSelect('13.12.13')
    appScreenCheck('prodStruct')
    # Site
    pyautogui.typewrite(site)
    pyautogui.press('enter')
    # Cost Set
    pyautogui.typewrite(costSet)
    pyautogui.press('enter')
    # Item (From: and To:)
    pyautogui.typewrite(item)
    pyautogui.press('tab')
    pyautogui.typewrite(item)
    for _ in range(16):
        pyautogui.press('tab')
    pyautogui.typewrite('c')
    for _ in range(2):
        pyautogui.press('enter')
    print('productStructureCostRollUp Completed')
    appScreenCheck('report')
    clearAppScreen()

def itemDataMaint(item, status):
    menuSelect('1.4.3')    
    appScreenCheck('dataMaint')
    # Item
    pyautogui.typewrite(item)
    for _ in range(2):
        pyautogui.press('enter')
    for _ in range(5):
        pyautogui.press('tab')
    pyautogui.typewrite(status)
    pyautogui.press('enter')
    print('costRollUp Completed')
    clearAppScreen()