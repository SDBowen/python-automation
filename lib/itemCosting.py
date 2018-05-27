import pyautogui

def freezeAndUnfreeze(site, costSet, item, status):
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

def costRollUp(site, costSet, item)
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

def elementCostCalc(item, costSet, freightPercent):
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
    
