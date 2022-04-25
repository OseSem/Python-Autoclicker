<<<<<<< HEAD
import pyautogui, keyboard, datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

=======
import pyautogui, time, threading, keyboard, sys
>>>>>>> f0ca2f848c19bdc958a222d2a66153b10eb57ac2

while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('b'):  # if key 'q' is pressed 
            pyautogui.rightClick()
<<<<<<< HEAD
            pyautogui.PAUSE = 0.025
            clicked_format = f"{bcolors.OKGREEN}{datetime.datetime.now().strftime('%m/%d/%Y [%H:%M:%S]')}{bcolors.OKCYAN} {bcolors.BOLD}Leftclicked 1 {bcolors.OKCYAN}time{bcolors.ENDC}"
            print(clicked_format)
        elif keyboard.is_pressed('n'):  # if key 'q' is pressed 
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.025
            clicked_format = f"{bcolors.OKGREEN}{datetime.datetime.now().strftime('%m/%d/%Y [%H:%M:%S]')}{bcolors.OKCYAN} {bcolors.BOLD}Rightclicked 1 {bcolors.OKCYAN}time{bcolors.ENDC}"
            print(clicked_format)
=======
            pyautogui.PAUSE = 0.001
>>>>>>> f0ca2f848c19bdc958a222d2a66153b10eb57ac2
    except:
        pass