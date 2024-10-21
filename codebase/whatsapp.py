import webbrowser  #toma el control de el navegador
import pyautogui as at #toma el control de el teclado para presionar enter
import time

def send_message(contact, message):
    webbrowser.open(f"https://web.whatsapp.com/send?phone={contact}&text={message}")
    time.sleep(15)
    at.press('enter')