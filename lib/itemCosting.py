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