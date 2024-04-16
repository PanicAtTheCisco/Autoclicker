from pynput import keyboard
from pynput.mouse import Button, Controller
import time
import threading

# Change these values to customize the autoclicker
rate = 0.001        # The rate at which the autoclicker clicks in seconds
toggleKey = 'q'     # The key that toggles the autoclicker

clicking = False

def toggle_autoclicker():
    global clicking
    clicking = not clicking
    print("Autoclicker toggled: " + str(clicking))

def click():
    while clicking:
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(rate)

def on_press(key):
    if key == keyboard.Key.esc:
        return False
    elif key == keyboard.KeyCode.from_char(toggleKey):
        toggle_autoclicker()
        threading.Thread(target=click).start()

mouse = Controller()

with keyboard.Listener(
    on_press=on_press) as listener:
    listener.join()
