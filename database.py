import json
import os

FILE = "resumes.json"


def load_data():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump([], f)
        return []

    try:
        with open(FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except:
        return []


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)