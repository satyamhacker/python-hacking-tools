
import pyautogui

import time


pyautogui.FAILSAFE = False

    
def write_command(write):
    pyautogui.write(write)
    
    
def press_execute_command(key):
    pyautogui.press(key)
    

def press_combination_keys(shortcut1,shortcut2):
    pyautogui.hotkey(shortcut1, shortcut2)
    
def sleep(sec):
    time.sleep(sec)
    
    
press_combination_keys('ctrl','esc')    

write_command("defender")

press_execute_command("enter")

sleep(3)

press_execute_command("space")
sleep(1)
press_execute_command("tab")
press_execute_command("tab")
press_execute_command("tab")
press_execute_command("tab")
press_execute_command("enter")
sleep(1)
press_execute_command("space")
sleep(2)

press_execute_command('left')
sleep(1)
press_execute_command('enter')
sleep(1)

press_combination_keys('alt','f4')    

