import pyautogui
import time

def mesaj():
    message = "MERHABA BEN MUHARREM"
    pyautogui.typewrite(message)
    pyautogui.press("enter")

time.sleep(10)

for _ in range(10):
    mesaj()
    time.sleep(1)  

  

