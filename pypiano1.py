
from pynput.keyboard import Key, Controller
import time
import pyautogui
#import keyboard


import threading
time.sleep(2)
import threading




def press_key_for_time(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)


def press_shift_key_for_time(key, duration):
    k = Controller()
    k.press(Key.shift)
    k.press(key)
    time.sleep(duration)
    k.release(key)
    k.release(Key.shift)

def right_thumb_task():
    
    
def right_index_task():
    ...
    
def right_middle_task():
    ...

def right_ring_task():
    ...
    
def right_pinky_task():
    ...
    
def left_thumb_task():
    ...
    
def left_index_task():
    ...
    
def left_middle_task():
    ...
    
def left_ring_task():
    ...
    
def left_pinky_task():
    ...

# create separate threads for each finger task
right_thumb_thread = threading.Thread(target=right_thumb_task)
right_index_thread = threading.Thread(target=right_index_task)
right_middle_thread = threading.Thread(target=right_middle_task)
right_ring_thread = threading.Thread(target=right_ring_task)
right_pinky_thread = threading.Thread(target=right_pinky_task)
left_thumb_thread = threading.Thread(target=left_thumb_task)
left_index_thread = threading.Thread(target=left_index_task)
left_middle_thread = threading.Thread(target=left_middle_task)
left_ring_thread = threading.Thread(target=left_ring_task)
left_pinky_thread = threading.Thread(target=left_pinky_task)

right_thumb_thread.start()
right_index_thread.start()
right_middle_thread.start()
right_ring_thread.start()
right_pinky_thread.start()
left_thumb_thread.start()
left_index_thread.start()
left_middle_thread.start()
left_ring_thread.start()
left_pinky_thread.start()
