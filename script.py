import win32con  # this lib was used to send command key up and key down, like when you press any key
import pygetwindow as gw  # this lib was used to get the handle by aplication's title
from threading import Thread  # this lib was used to create a thread
from win32gui import SendMessage  # This lib was used to send keystrokes
from random import randint, choice # this lib was used to generate a random numbers in "loop for" and choose one random value, respectively
from mousekey import MouseKey # this lib was used to make a safe stop key(ctrl+e)
from time import sleep  # this lib was used to pause for a while in seconds.... I don't know of any other simpler way to explain what is already simple
import pyautogui  # this lib was used to and just to send a spam message if you try execute the script more than once


# variables
POSSIBILITIES = [
    2.8,
    3,
    3.5,
                 3.8,
                 4,
                 4.5
                 ]
execution = 0

# Take the handle based on windows title
def handle_of_windowtitle(title):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        return window._hWnd
    except IndexError:
        return None
  
  
# the script function
def farm():
    # key for safe stop
    mkey = MouseKey()
    mkey.enable_failsafekill('ctrl+e')
    # take handle of aplication
    hwnd =  handle_of_windowtitle("NIGHT CROWS(1)")
    
    # send input Q (0x51) - start auto atack
    SendMessage(hwnd, win32con.WM_KEYDOWN, 0x51, 0)
    sleep(0.01)
    SendMessage(hwnd, win32con.WM_KEYUP, 0x51 , 0)
    # send input Q (0x51) - start auto atack
    counter = 0
    # "infinite" loop for send inputs for a long long time....
    while True:
        counter += 1
        #  YOU NEED TO MAKE AN IN-GAME SETUP

        # send input U (ux55)
        SendMessage(hwnd,win32con.WM_KEYDOWN, 0x55 , 0)
        sleep(0.01)
        SendMessage(hwnd,win32con.WM_KEYUP, 0x55 , 0)
        
        # Loop to iterate on the mob
        for i in range(randint(2,4)):
            #  send input TAB (ux09)
            SendMessage(hwnd,win32con.WM_KEYDOWN, 0x09 , 0)
            SendMessage(hwnd,win32con.WM_KEYUP, 0x09 , 0)
            sleep(0.2)

        # At some point Char didn't focus on the mobs closest to him, for this problem, maybe this is the solution
        if counter >= 4:

            # send input U (ux55)
            SendMessage(hwnd, win32con.WM_KEYDOWN, 0x55, 0)
            sleep(0.01)
            SendMessage(hwnd, win32con.WM_KEYUP, 0x55, 0)
            counter = 0

        # sleep loop for random some time
        sleep(choice(POSSIBILITIES))

       
def main(): 
    global execution
    execution += 1
    if execution > 1:
        pyautogui.alert(title='Action denied!',
                        text='You have already started this function')
    # Create thread
    else:        
        # this line creat a thread of funcion farm
        start_farm = Thread(target=farm)
        # and this line starts it
        start_farm.start()

