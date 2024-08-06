import threading
import keyboard 
import  time
import pydirectinput

def key_press_sequence():
    while not stop_event.is_set():
        time.sleep(1)
        # 执行按键操作
        pydirectinput.keyDown('g')
        time.sleep(0.5)
        pydirectinput.keyUp('g')
        
        pydirectinput.keyDown('f')
        time.sleep(0.5)
        pydirectinput.keyUp('f')
        
        pydirectinput.keyDown('e')
        time.sleep(0.5)
        pydirectinput.keyUp('e')
        
        pydirectinput.keyDown('e')
        time.sleep(0.5)
        pydirectinput.keyUp('e')
        
        time.sleep(6)
        
        pydirectinput.keyDown('w')
        time.sleep(5.5)
        pydirectinput.keyUp('w')
        
        pydirectinput.keyDown('a')
        time.sleep(1.2)
        pydirectinput.keyUp('a')
        
        pydirectinput.keyDown('w')
        time.sleep(0.7)
        pydirectinput.keyUp('w')
        
        pydirectinput.keyDown('ctrl')
        time.sleep(0.5)
        pydirectinput.keyUp('ctrl')

        time.sleep(5)

def start_task():
    global stop_event
    stop_event.clear()
    thread = threading.Thread(target=key_press_sequence)
    thread.start()

def stop_task():
    global stop_event
    stop_event.set()

stop_event = threading.Event()

print("Press Enter to start the task...")
keyboard.wait('enter')  # 等待按下回车键
start_task()

print("Press ESC key to stop the task...")
keyboard.wait('esc')  # 等待按下向下键
stop_task()
print("Task stopped.")
