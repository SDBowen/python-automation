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
    supplierList = []

    menuSelect.menuSelect('28.20.1.1')
    appScreenCheck.appScreenCheck('supplierCreate')  # THIS NEEDS TO BE CREATED
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'c')
    for _ in range(2):
        pyautogui.press('tab')
    pyautogui.press(certification) # NEED VAR ASSIGNMENT
    for _ in range(2):
        pyautogui.press('tab')
    pyautogui.press('space') # NEED CONFIRM SCREEN AFTER THIS
    # Maximize app
    pyautogui.hotkey('alt', ' ', 'x')
    time.sleep(1) # Screen check instead?
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')
    pyautogui.typewrite(supplierName)
    pyautogui.typewrite(supplierSearchName) #28 char
    pyautogui.click(x=1600, y=650, button='right')
    for _ in range(2):
        pyautogui.press('down')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.typewrite(supplierAddressStreet)
    for _ in range(3):
        pyautogui.press('tab')
    pyautogui.typewrite(supplierAddressZip)
    pyautogui.press('tab')
    pyautogui.typewrite(supplierAddressCity)
    pyautogui.press('tab')
    pyautogui.typewrite(supplierAddressState)
    for _ in range(5):
        pyautogui.press('tab')
    pyautogui.typewrite(supplierPhone)
    pyautogui.press('tab')
    pyautogui.typewrite(supplierFax)
    pyautogui.press('tab')
    pyautogui.typewrite(supplierEmail)
    for _ in range(2):
        pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    for _ in range(2):
        pyautogui.press('right')
    pyautogui.press('tab')
    pyautogui.typewrite('APTRADE')
    pyautogui.press('tab')
    pyautogui.typewrite('APTRADE')
    pyautogui.press('tab')
    pyautogui.typewrite('APTRADE')
    # if Supplier type is needed
    for _ in range(10):
        pyautogui.press('tab')
    pyautogui.typewrite('CRF') # CRF EMP N-IC

    # Tab selection function

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