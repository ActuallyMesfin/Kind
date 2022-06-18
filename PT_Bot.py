from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(403, 500)[0] == 0:
        click(403, 500)
    if pyautogui.pixel(557, 500)[0] == 0:
        click(557, 500)
    if pyautogui.pixel(770, 500)[0] == 0:
        click(675, 500)
    if pyautogui.pixel(869, 500)[0] == 0:
        click(869, 500)
    
