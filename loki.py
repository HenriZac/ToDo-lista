from datetime import datetime

LOG_FILE = "tasks.log"


def kirjoita_loki(viesti):
    aika = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{aika}] {viesti}\n")

    except OSError:
        print("Virhe: lokitiedostoon kirjoittaminen epäonnistui.")