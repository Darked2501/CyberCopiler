import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def green(text):
    print(f"\033[32m{text}\033[0m")