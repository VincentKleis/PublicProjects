from pynput.keyboard import Key, Listener
from pyautogui import click
from time import sleep  

def on_press(key):
    
    # command on the tab key
    if key == Key.tab:
        return True

def on_release(key):

    if key == Key.esc:
        # Stop listener 
        return False

# Collect events until released
with Listener(
        on_press=on_press,  
        on_release=on_release) as listener:
    x = 120
    listener.join()
    while True:
        if x == 120:
            click()
        else:
            x += 1
            sleep(1)
