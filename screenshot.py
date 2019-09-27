import pyautogui
import time

x = 1

while x < 4: # number of screenshots 
    pyautogui.screenshot('/Users/macuser/Desktop/screenshot/image'+str(x)+'.png') #location to save the file
    x+=1 #while loop condition
    time.sleep(2) # every two seconds 
