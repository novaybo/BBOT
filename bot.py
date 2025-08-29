import pyautogui
import time
import sys
from pynput import keyboard
import threading



global Tab_times
Tab_times = 0
global screen_width, screen_height
screen_width, screen_height = pyautogui.size()

exit_event = threading.Event()
pause_event = threading.Event()

def on_press(key):
    if key == keyboard.Key.esc:
        exit_event.set()
    elif key == keyboard.Key.space:
        if pause_event.is_set():
            pause_event.clear()
            print("Resuming...")
        else:
            pause_event.set()
            print("Paused...")

listener = keyboard.Listener(on_press=on_press)
listener.start()

def wait_and_locate(i_p, confidence):
    """
    Waits for an image to appear on the screen and returns its position.
    
    :param i_p: Path to the image file to locate.
    :param confidence: Confidence level for image recognition (default is 0.8).
    :return: Position of the located image or None if not found.
    """
    global Tab_times
    position = None

    try:
        pyautogui.press("TAB")  # Press TAB to switch focus
        position = pyautogui.locateOnScreen(i_p, confidence=confidence)
        if position is not None:
            Tab_times = 0
            return position, 0
    except Exception as e:
        #Tab_times += 1
        return position, 0
    time.sleep(0.7)

    if Tab_times >= 5:
        start_x, start_y = screen_width // 2 + 200, screen_height // 2
        end_x, end_y = screen_width // 2 - 200, screen_height // 2
        pyautogui.moveTo(start_x, start_y)
        pyautogui.mouseDown(button="right")
        time.sleep(0.1)
        pyautogui.keyDown("w")
        pyautogui.dragTo(end_x, end_y, duration=2)
        pyautogui.keyUp("w")
        pyautogui.mouseUp(button="right")
        Tab_times = 0
    return None, 0

def press_key_multiple_times(key, times, delay):
    """
    Presses a key multiple times.
    
    :param key: The key to press.
    :param times: Number of times to press the key (default is 1).
    """
    for _ in range(times):
        pyautogui.press(key)
        time.sleep(delay)  # Small delay between presses

def sale_event():
    try:
        position = pyautogui.locateOnScreen("/home/dante/VSCode/.venv/projects/BBOT/Screenshot_20250821_204425.png", confidence=0.7)
    except:
        position = None
    if position is not None:
        pyautogui.click(position[0] + 56 , position[1] + 50)
        try:
            position1 = pyautogui.locateOnScreen("/home/dante/VSCode/.venv/projects/BBOT/Screenshot_20250821_214558.png", confidence=0.7)
        except:
            position1 = None
        if position1 is not None:
            pyautogui.click(position1[0] + 5, position1[1] + 3)
            sys.exit()
    else:
        start_x, start_y, end_x, end_y = screen_width // 2 + 200, screen_height // 2, screen_width // 2 , screen_height // 2
        pyautogui.moveTo(start_x, start_y)
        time.sleep(0.1)
        pyautogui.dragTo(end_x, end_y, duration=2, button="right")

def image_action(i_p, confidence):

    while not exit_event.is_set():

        try:
            position, gate = wait_and_locate(i_p, confidence)
            if exit_event.is_set():
                break
            if gate == 1:
                if position is not None:
                    press_key_multiple_times("1", 1, 0.3)
                else:
                    print("Image not found.")
            elif gate == 0:
                sale_event()
        except Exception as e:
            print(f"An error occurred while processing the image action: {e}")
            pass

def dungeon_mode():

    while not exit_event.is_set():
        if not pause_event.is_set():
            press_key_multiple_times("1", 1, 0.2)
            press_key_multiple_times("2", 10, 0.2)
        else:
            print("Paused... Press Space to resume.")
            time.sleep(1)

def main():

    mode = input("Choose mode: \n 1. Farm \n 2. Dungeon \n")

    # Move the mouse to the center of the screen
    pyautogui.moveTo(screen_width // 2, screen_height // 2)

    if mode == "1":
        time.sleep(3)
        image_action("/home/dante/VSCode/.venv/projects/BBOT/Screenshot_20250821_014922.png", confidence=0.7)
    elif mode == "2":
        time.sleep(3)
        dungeon_mode()
    else:
        print("Invalid mode selected. Exiting.")

main()