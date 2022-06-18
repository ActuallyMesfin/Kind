# A program that can play magic piano tiles

import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Defining what a click should do
def click(x, y):
    # Set the position to specified coordinates
    win32api.SetCursorPos((x,y))
    # Press down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #Wait a while and then let go
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# The main code

# ADDED: Made it a forever loop to allow you to exit and enter the program with out having to rerun
# If s is pressed the program starts
# If q is pressed the program stops
# Use ctrl C to truly exit the program

# Issue: The coordinates for the points to press depend on what the program/website you are using.
# I used: https://www.agame.com/game/magic-piano-tiles
while True:
    if keyboard.is_pressed('s') == True:
        while keyboard.is_pressed('q') == False:

            # If a pixel at () location is black, it is most likely a tile so click it.
            if pyautogui.pixel(300, 500)[0] == 0:
                click(300, 500)
            if pyautogui.pixel(400, 500)[0] == 0:
                click(400, 500)
            if pyautogui.pixel(500, 500)[0] == 0:
                click(500, 500)
            if pyautogui.pixel(600, 500)[0] == 0:
                click(600, 500)
