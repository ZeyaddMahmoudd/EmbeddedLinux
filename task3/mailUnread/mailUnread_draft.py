import pyautogui
import webbrowser
import time

def Firefox_yahoo():
    url = "https://www.yahoo.com"
    webbrowser.get('firefox').open(url)

def open_mail():
    image_path = "mail.png"
    image_location = pyautogui.locateCenterOnScreen(image_path, confidence = 0.7)
    if image_location is not None:
        pyautogui.click(image_location)
    else:
        print("Image not found on the screen")
    

Firefox_yahoo()
time.sleep(10)
open_mail()
