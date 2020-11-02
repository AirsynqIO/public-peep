import os

ASSETS_FOLDER = f"{os.getcwd()}/assets"


def init():
    if not os.path.exists(ASSETS_FOLDER):
        os.makedirs(ASSETS_FOLDER)


def asset_path(filename):
    return f'{ASSETS_FOLDER}/{filename}'


def delete_asset(filename):
    os.unlink(f"{ASSETS_FOLDER}/{filename}")
