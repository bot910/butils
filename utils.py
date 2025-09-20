import os
import time
import random
import requests

def wait(amount):
    time.sleep(amount)

def current_time_millis():
    return int(round(time.time() * 1000))

def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

def random_choice(choices):
    return random.choice(choices)

def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for i in range(length))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_file(url, dest):
    response = requests.get(url)
    with open(dest, 'wb') as file:
        file.write(response.content)
