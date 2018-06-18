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
    x, y = pyautogui.locateCenterOnScreen('images/businessRelationTab.png', grayscale='true')
    pyautogui.click(x, y)
    pyautogui.press('right')
    # accounting
    # payment
    pyautogui.press('tab')
    pyautogui.typewrite(supplierTerms)
    pyautogui.press('tab')    
    pyautogui.typewrite(supplierInvoiceStatus) #S-NOPO, S-POINV
    # banking
    pyautogui.click(x=1600, y=650, button='right')
    for _ in range(4):
        pyautogui.press('up')
    pyautogui.press('space')
    pyautogui.press('tab')    
    pyautogui.typewrite('XX')
    for _ in range(2):
        pyautogui.press('tab') 
    pyautogui.typewrite('07192328417519932218765317760')
    pyautogui.press('tab')
    pyautogui.hotkey('alt', ' ')
    pyautogui.press('x')    
    time.sleep(1) # Screen check instead?
    # need payment selection logic

    # default
    # tax info
    for _ in range(3):
        pyautogui.press('tab')
    pyautogui.typewrite(supplierTaxId)
    for _ in range(11):
        pyautogui.press('tab')
    pyautogui.press('space')
    print('Done')

makeSupplierInactive()