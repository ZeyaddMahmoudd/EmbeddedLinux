import pyautogui
import webbrowser
import time

def Firefox_yahoo():
    url = "https://www.yahoo.com"
    webbrowser.get('firefox').open(url)

def open_mail():
    image_path = "/home/zeyad/Desktop/embeddedlinuxtasks/task3/mailUnread/mailUnread_mailScreenshot.png"
    image_location = None
    while image_location == None:
        image_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
    pyautogui.click(image_location)
    print("mail button found")

def mark_as_read():

    #dropdown menu arrow location
    pyautogui.click(x=262, y=299)

    #locate mark emails as read and press it
    image_path = "/home/zeyad/Desktop/embeddedlinuxtasks/task3/mailUnread/mailUnread_markEmailsAsRead.png"
    image_location = None
    while image_location == None:
        image_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
    pyautogui.click(image_location)
    print("mark emails as read button found")


Firefox_yahoo()
open_mail()
time.sleep(10)
mark_as_read()




