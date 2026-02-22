from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import threading

# 创建键盘和鼠标控制器
keyboard_controller = KeyboardController()
mouse_controller = MouseController()

def shift_right_click(x=None, y=None):
    keyboard_controller.press(Key.shift)
    time.sleep(0.1)
    mouse_controller.press(Button.right)
    time.sleep(0.1)
    keyboard_controller.release(Key.shift)
    time.sleep(0.1)
    mouse_controller.release(Button.right)

    time.sleep(0.5)
    mouse_controller.press(Button.right)
    time.sleep(0.1)
    mouse_controller.release(Button.right)

def shift_f():
    keyboard_controller.press(Key.shift)
    time.sleep(0.1)
    keyboard_controller.press('f')
    time.sleep(0.2)
    keyboard_controller.release(Key.shift)
    time.sleep(0.1)
    keyboard_controller.release('f')

    time.sleep(0.3)
    mouse_controller.press(Button.left)
    time.sleep(0.2)
    mouse_controller.release(Button.left)

def combo():
    shift_right_click()
    time.sleep(0.2)
    shift_left_click()

def combo1():
    shift_f()
    time.sleep(0.5)
    keyboard_controller.press('f')
    time.sleep(0.1)
    keyboard_controller.release('f')



def shift_left_click():
    keyboard_controller.press(Key.shift)
    time.sleep(0.1)
    mouse_controller.press(Button.left)
    time.sleep(0.4) 
    keyboard_controller.release(Key.shift)
    time.sleep(0.05)
    mouse_controller.release(Button.left)
   





def on_press(key):
    try:
        # 检查是否按下了数字1键
        if key.char == '1':
            print("检测到1键被按下，触发Shift+右键点击")
            thread = threading.Thread(target=combo)
            thread.daemon = True
            thread.start()
        elif key.char == '2':
            print("检测到1键被按下，触发Shift+右键点击")
            thread = threading.Thread(target=combo1)
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