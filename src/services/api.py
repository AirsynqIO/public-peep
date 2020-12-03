import threading

import requests

MODEL_URL = "https://whatever-sogo-wants.com"


def send_file(filepath):
    files = {'image': open(filepath, 'rb')}
    requests.post(MODEL_URL, files=files)


def send_file_async(filepath):
    proc = threading.Thread(target=send_file, args=(filepath,))
    proc.start()
