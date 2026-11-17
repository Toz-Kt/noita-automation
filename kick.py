from pynput import keyboard
import pyautogui
import time

last_time = 0
cooldown = 0.8

def al_presionar_tecla(key):
    global last_time
    try:
        if key.char == "x":
            tiempo_actual = time.time()
            if tiempo_actual - last_time > cooldown:
                time.sleep(0.110)
                pyautogui.click()
                last_time = time.time()
            else:
                print("Calmado, la macro está en cooldown xd")
    except AttributeError:
        pass
    last_time = time.time()
with keyboard.Listener(on_press=al_presionar_tecla) as listener:
    listener.join()