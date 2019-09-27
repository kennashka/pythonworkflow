import pyautogui
import time

x = 1

while x < 4:
pyautogui.screenshot('/Users/macuser/Desktop/screenshot/image'+str(x)+'.png')
x+=1
time.sleep(2)
