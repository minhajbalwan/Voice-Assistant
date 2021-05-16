from pyautogui import click
from keyboard import press, write
from time import sleep
import webbrowser

def WhatsappName(name):
    webbrowser.open('https://web.whatsapp.com/')
    sleep(20)
    click(x=237, y=185)
    sleep(1)
    write(name)
    sleep(1)
    press('enter')

def WhatsappMsg(message):
    click(x=741, y=700)
    sleep(1)
    write(message)
    sleep(1)
    press('enter')
    print('message sent')