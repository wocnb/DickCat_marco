from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import threading

# 创建键盘和鼠标控制器
keyboard_controller = KeyboardController()
mouse_controller = MouseController()

def s_e():
    keyboard_controller.press('s')
    time.sleep(0.01)
    keyboard_controller.press('e')
    time.sleep(0.1)
    keyboard_controller.release('s')
    time.sleep(0.5)
    time.sleep(2.3)
    time.sleep(1)
    keyboard_controller.release('e')

def w_e():
    keyboard_controller.press('w')
    time.sleep(0.01)
    keyboard_controller.press('e')
    time.sleep(0.1)
    keyboard_controller.release('w')
    time.sleep(0.5)
    time.sleep(1.5)
    time.sleep(0.2)
    keyboard_controller.release('e')
    

def shift_e():
    keyboard_controller.press(Key.shift)
    time.sleep(0.1)
    keyboard_controller.press('e')
    time.sleep(0.1)
    keyboard_controller.release(Key.shift)
    time.sleep(3)
    keyboard_controller.release('e')

def full_combo():
    # while True:
        s_e()
        time.sleep(0.1)
        w_e()
        time.sleep(0.8)
        shift_e()
        time.sleep(1)
    


def on_press(key):
    try:
        if key.char == '1':
            print("检测到1键被按下，触发Shift+右键点击")
            thread = threading.Thread(target=full_combo)
            thread.daemon = True
            thread.start()
    except AttributeError:
        pass

def on_release(key):
    if hasattr(key, 'char') and key.char == '=':
        print("检测到等号键被按下，停止监听")
        return False

def start_keyboard_listener():
    print("开始监听键盘... 按下1键触发Shift+右键，按Esc键退出")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keyboard_listener()