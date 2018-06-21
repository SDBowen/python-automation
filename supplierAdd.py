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

cert = 'A'
supplierName = 'test'
supplierSearchName = 'test-370-'
supplierAddressStreet = 'Test'
supplierAddressZip = '11111'
supplierAddressCity = 'Test'
supplierAddressState = 'TX'
supplierPhone = '1234567'
supplierFax = '1-234-567-8910'
supplierEmail = 'test@test.com'
supplierTerms = 'N60'
supplierInvoiceStatus = 'S-NOPO'
supplierTaxId = '11111-11111'
supplierPaymentType = 'US-PM-CHK-AP'



def createNewSupplier(cert, supplierName, supplierSearchName, supplierAddressStreet, supplierAddressZip, supplierAddressCity, supplierAddressState, supplierPhone, supplierFax, supplierEmail, supplierTerms, supplierInvoiceStatus, supplierTaxId, supplierPaymentType):
    
    menuSelect.menuSelect('28.20.1.1')
    appScreenCheck.appScreenCheck('supplierCreate') 
    pyautogui.press('tab')
    pyautogui.keyDown('shift')
    pyautogui.press('tab')
    pyautogui.keyUp('shift')
    pyautogui.hotkey('ctrl', 'c')
    for _ in range(2):
        pyautogui.press('tab')
    pyautogui.press(cert)
    for _ in range(2):
        pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.hotkey('alt', ' ')
    pyautogui.press('x')    
    appScreenCheck.appScreenCheck('businessRelationCreate')
    # Maximize app
    pyautogui.hotkey('alt', ' ')
    pyautogui.press('x')    
    appScreenCheck.appScreenCheck('businessRelationAddress') # Can open on wrong screen
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')
    pyautogui.typewrite(supplierName)
    pyautogui.press('tab')
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
    # accounting
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
    appScreenCheck.appScreenCheck('businessRelationTab')
    pyautogui.click(370, 250)
    for _ in range(2):
        pyautogui.press('right')
    # payment
    pyautogui.press('tab')
    pyautogui.typewrite(supplierTerms)
    for _ in range(2):
        pyautogui.press('tab')    
    pyautogui.typewrite(supplierInvoiceStatus) #S-NOPO, S-POINV
    # banking
    pyautogui.click(370, 250)
    for _ in range(3):
        pyautogui.press('right')
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
    # Maximize
    pyautogui.hotkey('alt', ' ')
    pyautogui.press('x')    

    appScreenCheck.appScreenCheck('bankPayment')
    # need payment selection logic
    pyautogui.click(75, 100)
    pyautogui.press('a')    
    pyautogui.press('p')    
    pyautogui.press('tab')    
    pyautogui.press('e')    
    pyautogui.press('tab')    
    pyautogui.typewrite(supplierPaymentType)
    pyautogui.press('enter')    
    time.sleep(3)
    pyautogui.press('enter')    

    # tax info
    pyautogui.click(370, 250)
    for _ in range(5):
        pyautogui.press('right')
    for _ in range(3):
        pyautogui.press('tab')
    pyautogui.typewrite(supplierTaxId)
    for _ in range(11):
        pyautogui.press('tab')
    #pyautogui.press('space')
    print('Done')

createNewSupplier(cert, supplierName, supplierSearchName, supplierAddressStreet, supplierAddressZip, supplierAddressCity, supplierAddressState, supplierPhone, supplierFax, supplierEmail, supplierTerms, supplierInvoiceStatus, supplierTaxId, supplierPaymentType)