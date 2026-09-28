import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Virhe: tehtävätiedosto ei ole kelvollinen JSON-tiedosto.")
        return []


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        return True
    except OSError:
        print("Virhe: tehtävien tallennus epäonnistui.")
        return False