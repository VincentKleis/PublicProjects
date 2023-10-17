from pynput.keyboard import Key, Listener
import pyautogui
from time import sleep

def on_press(key):
    
    # command on the tab key
    if key == Key.shift:
        
        # find the location of your item
        '''
        count = 0
        x, y = pyautogui.position()
        while count<=1:
            if count == 0:
                print(f"'position{count}X' : {x},", end= ' ')
                count += 1
            if count == 1:
                print(f"'position{count}Y' : {y},")
                count += 1
        '''
        # presses spell then item
        pyautogui.click(1844, 851)
        sleep(0.1)
        pyautogui.click(1742, 761)

def on_release(key):

    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,  
        on_release=on_release) as listener:
    listener.join()   