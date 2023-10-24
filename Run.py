import os
import keyboard
import subprocess
import time
from colorama import init, Fore, Back, Style

overlay_path = r"%appdata%\dx9ware\overlay.exe"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def terminate():
    try:
        subprocess.run(['taskkill', '/f', '/im', 'overlay.exe'], check=True)
    except subprocess.CalledProcessError:
        pass

def run():
    subprocess.Popen(overlay_path, shell=True)

def color():
    init(autoreset=True)
    text = "Press F2 to terminate and F3 to run dx9ware overlay"

    while True:
        clear()
        print(Fore.GREEN + text)
        time.sleep(0.1)

keyboard.add_hotkey('F2', terminate)
keyboard.add_hotkey('F3', run)

try:
    print("Press F2 to terminate and F3 to run dx9ware overlay")
    color()
    keyboard.wait()
except KeyboardInterrupt:
    pass
