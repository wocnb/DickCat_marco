from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import threading

# 创建键盘和鼠标控制器
keyboard_controller = KeyboardController()
mouse_controller = MouseController()

def denfese_reduse():
    keyboard_controller.press('w')
    time.sleep(0.1)
    keyboard_controller.press('f')
    time.sleep(0.2)
    keyboard_controller.release('w')
    time.sleep(0.1)
    keyboard_controller.release('f')
    
    time.sleep(1.4)

    keyboard_controller.press(Key.shift)
    time.sleep(0.1)
    keyboard_controller.press('q')
    time.sleep(0.1)
    keyboard_controller.release(Key.shift)
    keyboard_controller.release('q')

def defence_increase():
    keyboard_controller.press(Key.shift)
    time.sleep(0.1)
    keyboard_controller.press('f')
    time.sleep(0.1)
    keyboard_controller.release(Key.shift)
    keyboard_controller.release('f')

    time.sleep(1.5)

    keyboard_controller.press(Key.shift)
    time.sleep(0.1)
    mouse_controller.press(Button.right)
    time.sleep(0.1)
    keyboard_controller.release(Key.shift)
    mouse_controller.release(Button.right)

    time.sleep(0.9)

    keyboard_controller.press(Key.shift)
    time.sleep(0.1)
    keyboard_controller.press('e')
    time.sleep(0.1)
    keyboard_controller.release(Key.shift)
    keyboard_controller.release('e')

def z_suit():
    denfese_reduse()
    time.sleep(1.28)
    defence_increase()

def suss_mode_combo_static():
    mouse_controller.press(Button.left)
    time.sleep(0.1)
    mouse_controller.release(Button.left)

    time.sleep(0.6)

    mouse_controller.press(Button.right)
    time.sleep(0.1)
    mouse_controller.release(Button.right)

    time.sleep(0.7)

    keyboard_controller.press(Key.space)
    time.sleep(0.1)
    keyboard_controller.release(Key.space)

def suss_mode_combo(target = '2'):
    if target == '2':
        mouse_controller.press(Button.right)
        time.sleep(0.1)
        mouse_controller.release(Button.right)
        time.sleep(0.9)
    elif target == '3':
        keyboard_controller.press('w')
        time.sleep(0.01)
        mouse_controller.press(Button.right)
        time.sleep(0.1)
        keyboard_controller.release('w')

        mouse_controller.release(Button.right)
        time.sleep(0.4)
    elif target == '4':
        keyboard_controller.press('s')
        time.sleep(0.01)
        mouse_controller.press(Button.right)
        time.sleep(0.1)
        keyboard_controller.release('s')

        mouse_controller.release(Button.right)
        time.sleep(0.45)

    suss_mode_combo_static()

    time.sleep(1)

    if target == '2':
        keyboard_controller.press(Key.shift)
        time.sleep(0.1)
        mouse_controller.press(Button.right)
        time.sleep(0.1)
        keyboard_controller.release(Key.shift)
        time.sleep(0.1)
        mouse_controller.release(Button.right)
    elif target == '3':
        keyboard_controller.press(Key.shift)
        time.sleep(0.1)
        mouse_controller.press(Button.left)
        time.sleep(0.1)
        keyboard_controller.release(Key.shift)
        time.sleep(0.1)
        mouse_controller.release(Button.left)
    elif target == '4':
        keyboard_controller.press(Key.shift)
        time.sleep(0.1)
        keyboard_controller.press('e')
        time.sleep(0.1)
        keyboard_controller.release(Key.shift)
        time.sleep(0.1)
        keyboard_controller.release('e')

def on_press(key):
    try:
        if key.char == '1':
            thread = threading.Thread(target=z_suit)
            thread.daemon = True
            thread.start()
        elif key.char in ['2', '3', '4']:
            thread = threading.Thread(target=suss_mode_combo, args=(key.char))
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