import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            print("Virhe: tehtavatiedosto on virheellinen.")
            return []

        valid_tasks = []

        for task in tasks:
            if not isinstance(task, dict):
                continue

            if "kuvaus" not in task:
                continue

            # Vanhat tehtävät saavat oletusarvot
            task.setdefault("tehty", False)
            task.setdefault("prioriteetti", "normaali")
            task.setdefault("deadline", "")

            valid_tasks.append(task)

        return valid_tasks

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Virhe: tehtavatiedosto on virheellinen.")
        return []

    except OSError:
        print("Virhe: tehtavatiedoston lukeminen epaonnistui.")
        return []


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(
                tasks,
                file,
                ensure_ascii=False,
                indent=4
            )

        return True

    except OSError:
        print("Virhe: tehtavien tallentaminen epaonnistui.")
        return False