# BLUM Airdrop Auto Click - President trump/kamala
# First created by Dymles Ganz
# Autorun version: A.P

from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
from termcolor import colored
import win32gui
import win32process
import ctypes
import os
import sys

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible


mouse = Controller()
time.sleep(0.5)

path = os.getcwd()

def anjaymabar():
    print("""
   |      |                         |             |   
   __ \   |  |   |  __ `__ \        __ \    _ \   __| 
   |   |  |  |   |  |   |   | _____ |   |  |   )  |  |   
  _.__/  _| \__,_| _|  _|  _|       _.__/  \___/  \__| 
    """)

anjaymabar()
print("  From Author: Dymles Ganz")
print("  Contact telegram: @BraveXploiter")
print("  Donations USDT (TRC20): TYna9WAoVCAF2f7ynnjS2bQixkLQz8XxFh")
print()
print("  Autorun Author: A.P")
print("  Donations USDT (TRC20): TBSW2ubNhspjxtosXPn7jB73HC53rK9soE")

language_choice = 1

if language_choice == 1:
    window_input = "\n blumbot@app:~# "
    window_not_found = " Your Window - {} not found!"
    window_found = " Window found! - {}\n Now bot working... Press 'K' on the keyboard to pause."
    pause_message = " Bot paused...\n Press 'K' again in the keyboard to continue"
    continue_message = " Bot continue working..."

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

window_name = "1"

if window_name == '1':
    window_name = "Mini App: Blum"

def most_common_used_color(img):
    width, height = img.size

    # Initialize Variable
    r_total = 0
    g_total = 0
    b_total = 0

    count = 0

    # Iterate through each pixel
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))

            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total/count, g_total/count, b_total/count)


def pixel_condition(r, g, b):
    return ((r in range(200, 255) and g in range(34, 65) and b in range(184, 200)) or          # candy
            (r in range(87, 129) and g in range(160, 203) and b in range(23, 60)) or          # berries
            (r in range(209, 239) and g in range(0, 14) and b in range(149, 167)) or          # head
            (r in range(234, 234) and g in range(250, 251) and b in range(120, 122)) or       # head
            (r in range(132, 180) and g in range(56, 88) and b in range(7, 38)) or            # gingerbread
            (r in range(43, 58) and g in range(88, 111) and b in range(24, 36)) or            # tree
            (r in range(176, 183) and g in range(236, 242) and b in range(250, 255)) or       # candle
            (r in range(196, 255) and g in range(15, 32) and b in range(172, 195)))           # boots


def waitGame():
    try:
        cords = pyautogui.locateOnScreen(path+'\\reward.PNG')
        buttonpoint = pyautogui.center(cords)
        print(buttonpoint)
        return True
    except:
        return False


check = gw.getWindowsWithTitle(window_name)
#print(gw.getAllTitles())
if not check:
    print(window_not_found.format(window_name))
    print("EN:\n   Make sure you use the TelegramDesktop application (not Telegram Web).\n   And have opened the Blum bot on your TelegramDesktop.\n   Until the Blum window is available")
    input("\n Press 'ENTER' to exit...")
else:
    print(window_found.format(window_name))
    telegram_window = check[0]
    paused = False
    timet = 0
    t = time.time()
    last_t = 0
    while True:
        last_t = t
        if keyboard.is_pressed('K'):
            paused = not paused
            if paused:
                print(pause_message)
            else:
                print(continue_message)
            time.sleep(0.2)

        if paused:
            continue

        window_rect = (
            telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
        ) 

        if telegram_window != []:
            try:
                telegram_window.activate()
            except:
                telegram_window.minimize()
                telegram_window.restore()

        scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))
        timet += 1
        width, height = scrn.size
        pixel_found = False
    
    
        if pixel_found:
            break

        for x in range(0, width, 13):
            for y in range(0, height, 13):
                r, g, b = scrn.getpixel((x, y))                
                if (63 <= r <= 73) and (219 <= g <= 229) and (0 <= b <= 10):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    timet -= 1
                    break

                elif (226 <= r <= 236) and (170 <= g <= 180) and (131 <= b <= 141):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    timet -= 1
                    break

                elif (255 <= r <= 265) and (137 <= g <= 147) and (97 <= b <= 107):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    timet -= 1
                    break

                elif pixel_condition(r,g,b):
                    screen_x = window_rect[0] + x
                    screen_y = window_rect[1] + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    timet -= 1
                    break
        
        t = time.time()
        print(str(t)+"\t|\t"+str(last_t)+"\t|\t"+str(timet))
        if timet > 200:    
            paused = not paused
            try:
                cords = pyautogui.locateOnScreen(path+'\\play.png')
                buttonpoint = pyautogui.center(cords)
                print(buttonpoint)
                pyautogui.moveTo(buttonpoint)
                pyautogui.click(buttonpoint)
                paused = not paused
                timet = 0
            except:
                #print("Đang chơi")
                try:
                    time.sleep(20)
                    cords = pyautogui.locateOnScreen(path+'\\choose.png')
                    buttonpoint = pyautogui.center(cords)
                    print(buttonpoint)
                    pyautogui.moveTo(buttonpoint)
                    pyautogui.click(buttonpoint)
                    time.sleep(20)
                    cords = pyautogui.locateOnScreen(path+'\\reload.png')
                    buttonpoint = pyautogui.center(cords)
                    print(buttonpoint)
                    pyautogui.moveTo(buttonpoint)
                    pyautogui.click(buttonpoint)
                    paused = not paused
                    timet = 0
                except:
                    print("Button's not found")
