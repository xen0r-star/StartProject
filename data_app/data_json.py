import json

def save_data(data):
    with open("data_app/data.json", "w") as file:
        json.dump(data, file)

def load_data():
    try:
        with open("data_app/data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None
    


def load_info():
    with open("data_app/info.json", "r") as file:
        data = json.load(file)
        return data
