import pyautogui
import time

def mesaj():
    message = "MERHABA BEN MUHARREM"   #Siz istediğiniz kelime veya cümleyi buraya yazabilirsiniz.
    pyautogui.typewrite(message)
    pyautogui.press("enter")

time.sleep(10)

while True:

    mesaj()
    time.sleep(1)  



