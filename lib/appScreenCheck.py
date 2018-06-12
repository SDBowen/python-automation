import pyautogui

def appScreenCheck(screenType):
    type_dict = {'report': 'images/report.png', 'freezeUnfreeze': 'images/freeze.png', 'routing': 'images/routing.png', 'element': 'images/itemElement.png', 'overhead': 'images/itemOverhead.png', 'prodStruct': 'images/prodStruct.png', 'dataMaint': 'images/itemMaint.png', 'supplierBrowse': 'images/supplierBrowse.png', 'supplierModify': 'images/supplierModify.png', 'supplierModify2': 'images/supplierModify2.png', 'itemSiteCostMaint': 'images/itemSiteCostMaint.png'}
    img = type_dict[screenType]
    # Report completion image
    runComplete = pyautogui.locateOnScreen(img, region=(0, 0 , 1920, 200), grayscale=True)
    # Check for menu run completion
    while runComplete == None:
        runComplete = pyautogui.locateOnScreen(img, region=(0, 0 , 1920, 200), grayscale=True)
        print('Waiting for screen match...')
    print('Screen Check: OK!')