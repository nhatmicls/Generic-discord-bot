import imp


import random

from typing import *


def multi_data_to_messeage(input: Dict[str, str]) -> str:
    _send = ""
    for x in range(len(input)):
        _send += list(input)[x]
        _send += " = "
        _send += list(input.values())[x] + " "
        _send += "\n"
    return _send


def random_return(input: Dict[str, str]) -> str:
    response = random.choice(list(input.values()))
    return response
