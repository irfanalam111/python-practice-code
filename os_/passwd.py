import pyautogui
import itertools
import time
char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$*'
pass_wd=range(4,8)
for i in pass_wd:
    combination=itertools.product(char,repeat=i)
time.sleep(0)
for combo in combination:
    password = "".join(combo)
    pyautogui.typewrite(combo)
    pyautogui.press("enter")

