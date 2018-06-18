from appIsOpenCheck import appIsOpenCheck
from lib import clearAppScreen
from lib import menuSelect
from lib import appScreenCheck
import pyautogui, time

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
time.sleep(1)

clearAppScreen.clearAppScreen()

def makeSupplierInactive():
    supplierList = [504408,509666,500253,509665,500118]

    menuSelect.menuSelect('28.20.1.2')
    appScreenCheck.appScreenCheck('supplierBrowse')  
    for _ in range(3):
        pyautogui.press('tab')
    pyautogui.press('b')
    pyautogui.press('tab')
    pyautogui.press('e')   
    pyautogui.press('tab')
    for n in supplierList:
        pyautogui.typewrite(str(n))
        pyautogui.press('enter')
        while (pyautogui.pixelMatchesColor(950, 450, (255, 255, 255)) == False) and (pyautogui.pixelMatchesColor(275, 291, (65, 137, 238)) == False):
            print('#Check for supplier list: RGB not matched')
        time.sleep(1)
        pyautogui.press('enter')
        appScreenCheck.appScreenCheck('supplierModify')
        appScreenCheck.appScreenCheck('supplierModify2')
        pyautogui.press('space')
        for _ in range(4):
            pyautogui.press('tab')
        for _ in range(2):
            pyautogui.press('space')
        appScreenCheck.appScreenCheck('supplierBrowse')
        for _ in range(5):
            pyautogui.press('tab')
        print(n)
    print('Done')

makeSupplierInactive()