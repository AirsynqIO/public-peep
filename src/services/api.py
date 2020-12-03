import threading

import requests

from src.services.assets import delete_file

MODEL_URL = "https://whatever-sogo-wants.com"


def send_file(filepath):
    files = {'image': open(filepath, 'rb')}
    requests.post(MODEL_URL, files=files)
    delete_file(filepath)


def send_file_async(filepath):
    proc = threading.Thread(target=send_file, args=(filepath,))
    proc.start()
