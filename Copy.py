import pyperclip
import keyboard as key
import time


while True:
    time.sleep(0.01)
    if key.is_pressed('ctrl') and key.is_pressed('c'):
        time.sleep(0.05)
        with open("D:\\Residual Information\\pasteList", 'a') as file:
            file.seek(2)
            file.write(pyperclip.paste())
            file.write('\n')
        while key.is_pressed('ctrl') or key.is_pressed('c'):
            pass
