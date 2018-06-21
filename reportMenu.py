#! python3
import pyautogui
import time
from appIsOpenCheck import appIsOpenCheck
from lib import clearAppScreen
from lib import menuSelect

# Input from user

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

# Select menu search
pyautogui.hotkey('ctrl', 'm', 'delete')
# Enter menu input from user
pyautogui.typewrite('55.3.21.3', .15)
pyautogui.press('enter')
pyautogui.press('esc')
time.sleep(3)
# Check for report screen
while pyautogui.pixelMatchesColor(1800, 855, (255, 255, 255)) == True and pyautogui.pixelMatchesColor(1800, 830, (255, 255, 255)) == True:
    print('#Waiting for report screen')

time.sleep(2)
pyautogui.click(350, 160)
for _ in range(4):
    pyautogui.press('tab')
pyautogui.press('space')
pyautogui.click(350, 160)
for _ in range(5):
    pyautogui.press('tab')
pyautogui.press('space')

pyautogui.press('tab')
pyautogui.press('e')
pyautogui.press('tab')
pyautogui.typewrite('6/21/2018')
for _ in range(2):
    pyautogui.press('tab')
pyautogui.press('space')

for _ in range(4):
    pyautogui.press('t')
pyautogui.press('tab')
pyautogui.press('e')
pyautogui.press('tab')
pyautogui.typewrite('iss-so')

for _ in range(4):
    pyautogui.press('tab')
pyautogui.press('a')
pyautogui.click(900, 155)

time.sleep(5) # screen check
pyautogui.click(300, 105)
for _ in range(6):
    pyautogui.press('up')
pyautogui.press('space')

time.sleep(2) # screen check
pyautogui.press('f12')
time.sleep(2) # screen check
pyautogui.typewrite('filename')
for _ in range(10):
    pyautogui.press('tab')
pyautogui.press('space')
pyautogui.typewrite('C:\\Users\\sbowen\\Desktop\\Cost Dashboard')
pyautogui.press('enter')
for _ in range(14):
    pyautogui.press('tab')
pyautogui.press('space')



