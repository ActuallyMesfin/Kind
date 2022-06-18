from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Pos X:  419 Y:  500 RGB: (184, 188, 235)
#Tile 2 PosX:  551 Y:  500 RGB: (180, 183, 235)
#Tile 3 PosX:  693 Y:  500 RGB: (180, 183, 235)
#Tile 4 PosX:  781 Y:  500 RGB: (164, 169, 221)


def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(419, 500)[0] == 0:
        click(419, 500)
    if pyautogui.pixel(581, 500)[0] == 0:
        click(551, 500)
    if pyautogui.pixel(581, 500)[0] == 0:
        click(693, 500)
    if pyautogui.pixel(581, 500)[0] == 0:
        click(781, 500)
    
