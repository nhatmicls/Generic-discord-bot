import os
from typing import *
import json


class ReadDatabase:
    def __init__(self) -> None:
        pass

    def update_json_directory(self, json_file_direct):
        with open(json_file_direct, "r") as f:
            self.json_file = json.load(f)

    def get_random_messeage(self) -> Dict[str, str]:
        return self.json_file["random_chat"]

    def get_drive(self) -> Dict[str, str]:
        return self.json_file["google_drive"]

    def wake_up(self) -> Dict[str, str]:
        return self.json_file["wake_up"]
