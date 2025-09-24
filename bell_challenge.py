import pyautogui as pg
import time

pg.FAILSAFE = True
print("Move mouse to the top left to abort.")

#try:
#    while True:
#        x, y = pg.position()
#        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#        print(positionStr, end='')
#        print('\b' * len(positionStr), end='', flush=True) # Clears the line for continuous updates
#        time.sleep(0.05) # Adjust for desired update frequency
#except KeyboardInterrupt:
#    print('\n')

def send_email():
    Email_URL = "https://www.gmail.com"
    Email_To = "Michael.sekol@mahoningctc.com"
    subject = "Autopygui Email From John Swanson"
    Body = "I learned that pyautogui can make coding much easier and that you can do countless things with it."
    pg.moveTo(1343, 62)
#    time.sleep(0.05)
#    pg.click()
#    pg.moveTo(150, 218)
    time.sleep(0.05)
    pg.click()
    pg.click()
    pg.click()
    time.sleep(1)
    pg.write(Email_URL)
    time.sleep(1)
    pg.press("enter")
    time.sleep(1)
    pg.moveTo(150, 218)
    pg.click()
    time.sleep(1)
    pg.moveTo(1360, 476)
    pg.click()
    pg.write(Email_To)
    time.sleep(1)
    pg.moveTo(1769, 531)
    pg.click()
    pg.write(subject)
    time.sleep(1)
    pg.moveTo(1461, 613)
    pg.click()
    pg.write(Body)
    time.sleep(1)
    pg.moveTo(1301, 998)
    pg.click()

send_email()