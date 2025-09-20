import os
import sys
import time
import shutil
import random
import requests
from typing import Literal

#time utils
def wait(amount: float):
    time.sleep(amount)

def current_time_millis():
    return int(round(time.time() * 1000))

#random utils
def random_int(min_val: int, max_val: int):
    return random.randint(min_val, max_val)

def random_float(min_val: float, max_val: float):
    return random.uniform(min_val, max_val)

def random_choice(choices: list):
    return random.choice(choices)

def random_string(length: int):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(length))

#system utils
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program():
    sys.exit()

#file utils
def edit_file(file_path: str, option: Literal['rd', 're', 'cr', 'mk', 'de', 'rm', 'read', 'get', 'create', 'make', 'delete', 'remove']): 
    if option in ('rd', 're', 'read', 'get'):
        with open(file_path, 'r') as file:
            return file.read()
    elif option in ('cr', 'mk', 'create', 'make'):
        with open(file_path, 'x') as file:
            return file.write('')
    elif option in ('de', 'rm', 'delete', 'remove'):
        os.remove(file_path)
    else:
        raise ValueError("Invalid file option.")
    
def advanced_edit_file(file_path: str, option, extra):
    if option in ('wr', 'rp' 'write', 'replace'):
        with open(file_path, 'w') as file:
            return file.write(extra)
    elif option in ('ap', 'ad', 'append', 'add'):
        with open(file_path, 'a') as file:
            return file.write(extra)
    elif option in ('rm', 'dl', 'remove', 'delete'):
        if type(extra) == int:
            with open(file_path, 'r', encoding='utf-8') as text:
                content = text.read()
            if len(content) >= extra:
                content = content[:-extra]
                with open(file_path, 'w', encoding='utf-8') as text:
                    text.write(content)
            else:
                raise ArithmeticError("Cannot remove less characters that the file itself is.")
        elif type(extra) == str:
            pass
        else:
            raise TypeError("wrong type inputted")
    elif option in ('du', 'dp', 'duplicate', 'copy'):
        if not extra:
            raise ValueError("Destination path must be provided for duplicate operation.")
        shutil.copy(file_path, extra)
    elif option in ('mv', 'mo', 'move'):
        if not extra:
            raise ValueError("Destination path must be provided for move operation.")
        shutil.move(file_path, extra)

def file_exists(file_path: str): 
    return os.path.isfile(file_path)

#network utils
def fetch_json(url: str):
    response = requests.get(url)
    return response.json()

def fetch_text(url: str):
    response = requests.get(url)
    return response.text
    
def download_file(url: str, dest: str):
    response = requests.get(url)
    with open(dest, 'wb') as file:
        file.write(response.content)


edit_file("example.txt", "mk")
advanced_edit_file("example.txt", "wr", "Hello, World!")
print(edit_file("example.txt", "rd"))
advanced_edit_file("example.txt", "ap", "\nThis is an appended line.")
print(edit_file("example.txt", "rd"))
wait(2)
advanced_edit_file("example.txt", "du", "example_copy.txt")
advanced_edit_file("example_copy.txt", "rm", 400)
print(edit_file("example_copy.txt", "rd"))