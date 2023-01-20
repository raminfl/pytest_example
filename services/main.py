import random
import time

import requests

CONSTANT = 4

def get_number_one():
    return 1

def increment_num(a :int):
    return a+get_number_one()


def add_two_nums_plus_constant(a: int, b: int) -> int:
    return a+b+CONSTANT


def silly_get_request():
    params = {
        'timestamp': time.time(),
        'number': random.randint(1, 6)
    }
    response = requests.get('localhost:8000/get_data', params)
    if response.status_code == 200:
        return response.json()['args']



