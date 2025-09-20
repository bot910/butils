import os
import sys
import time
import random
import requests
from typing import Literal

#time utils
def wait(amount: int):
    time.sleep(amount)

def current_time_millis():
    return int(round(time.time() * 1000))

#random utils
def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

def random_choice(choices):
    return random.choice(choices)

def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(length))

#system utils
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program():
    sys.exit()

#file utils
def edit_file(file_path: str, option: Literal['r', 'read', 'w', 'write', 'replace', 'a', 'append', 'c', 'create', 'd', 'delete']): 
    if option == 'r' or 'read':
        with open(file_path, 'r') as file:
            return file.read()
    elif option == 'w' or 'write' or 'replace':
        with open(file_path, 'w') as file:
            return file.write()
    elif option == 'a' or 'append':
        with open(file_path, 'a') as file:
            return file.write()
    elif option == 'c' or 'create':
        with open(file_path, 'x') as file:
            return file.write()
    elif option == 'd' or 'delete':
        os.remove(file_path)
    else:
        raise ValueError("Invalid option. Use 'r', 'w', or 'a'.")

#network utils
def fetch_json(url):
    response = requests.get(url)
    return response.json()

def fetch_text(url):
    response = requests.get(url)
    return response.text
    
def download_file(url, dest):
    response = requests.get(url)
    with open(dest, 'wb') as file:
        file.write(response.content)

wait(0.5)