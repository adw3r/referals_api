import json
from pathlib import Path

from config import PACKAGE_FOLDER


# todo get values from table
def get_referrals_from_json() -> dict:
    path = Path(PACKAGE_FOLDER, 'referals.json')
    with open(path, 'rb') as file:
        texts_config = json.load(file)
        return texts_config
