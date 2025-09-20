import os
import sys
import time
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
def edit_file(file_path: str, option: Literal['rd', 're', 'wr', 'rp', 'ap', 'ad', 'cr', 'mk', 'de', 'rm', 'read', 'get', 'write', 'replace', 'append', 'add', 'create', 'make', 'delete', 'remove']): 
    if option in ('rd', 're', 'read', 'get'):
        with open(file_path, 'r') as file:
            return file.read()
    elif option in ('wr', 'rp' 'write', 'replace'):
        with open(file_path, 'w') as file:
            return file.write('')
    elif option in ('ap', 'ad', 'append', 'add'):
        with open(file_path, 'a') as file:
            return file.write('')
    elif option in ('cr', 'mk', 'create', 'make'):
        with open(file_path, 'x') as file:
            return file.write('')
    elif option in ('de', 'rm', 'delete', 'remove'):
        os.remove(file_path)
    else:
        raise ValueError("Invalid file option.")
    


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