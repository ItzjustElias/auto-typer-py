import pyautogui
import time

text = input("Give me the Text >>>")

time_interval = float(input("Give me the interval time >>>"))

time.sleep(4);

pyautogui.PAUSE = time_interval

charList = [ i for i in text ]

for char in charList:
    pyautogui.typewrite(char)