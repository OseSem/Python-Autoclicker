import pyautogui, time, threading, keyboard, sys

while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('b'):  # if key 'q' is pressed 
            pyautogui.rightClick()
            pyautogui.PAUSE = 0.001
    except:
        pass