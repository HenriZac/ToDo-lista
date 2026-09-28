from datetime import datetime
from loki import kirjoita_loki


def tyhjenna_naytto():
    print("\n" * 40)


def odota_enter():
    input("\nPaina Enter palataksesi...")


def otsikko(teksti):
    tyhjenna_naytto()
    print("=" * 40)
    print(f"{teksti:^40}")
    print("=" * 40)


def nayta_tehtavat(tasks):
    otsikko("KAIKKI TEHTÄVÄT")

    if not tasks:
        print("Ei tehtäviä.")
        odota_enter()
        return

    for i, tehtava in enumerate(tasks, start=1):
        tila = "[x]" if tehtava["tehty"] else "[ ]"
        prioriteetti = tehtava.get("prioriteetti", 2)
        deadline = tehtava.get("deadline", "")

        if prioriteetti == 1:
            prioriteetti_teksti = "Matala"
        elif prioriteetti == 2:
            prioriteetti_teksti = "Normaali"
        else:
            prioriteetti_teksti = "Korkea"

        deadline_teksti = deadline if deadline else "Ei määräpäivää"

        print(
            f"{i}. {tila} {tehtava['kuvaus']} "
            f"| Prioriteetti: {prioriteetti_teksti} "
            f"| Deadline: {deadline_teksti}"
        )

    odota_enter()


def lisaa_tehtava(tasks):
    otsikko("LISÄÄ TEHTÄVÄ")

    kuvaus = input("Tehtävän kuvaus: ").strip()

    if not kuvaus:
        print("Tehtävän kuvaus ei voi olla tyhjä.")
        odota_enter()
        return

    while True:
        print("\nPrioriteetti:")
        print("1 = Matala")
        print("2 = Normaali")
        print("3 = Korkea")

        prioriteetti = input("Valitse prioriteetti (1-3): ").strip()

        if prioriteetti in ("1", "2", "3"):
            prioriteetti = int(prioriteetti)
            break

        print("Virheellinen valinta. Anna numero 1, 2 tai 3.")

    while True:
        deadline = input(
            "\nMääräpäivä (YYYY-MM-DD, Enter = ei määräpäivää): "
        ).strip()

        if not deadline:
            break

        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Virheellinen päivämäärä. Käytä muotoa YYYY-MM-DD.")

    uusi_tehtava = {
        "kuvaus": kuvaus,
        "tehty": False,
        "prioriteetti": prioriteetti,
        "deadline": deadline
    }

    tasks.append(uusi_tehtava)

    kirjoita_loki(f"Lisättiin tehtävä: '{kuvaus}'")

    print("\nTehtävä lisätty.")
    odota_enter()


def merkitse_tehtava(tasks):
    otsikko("MERKITSE TEHTÄVÄ")

    if not tasks:
        print("Ei tehtäviä.")
        odota_enter()
        return

    for i, tehtava in enumerate(tasks, start=1):
        tila = "[x]" if tehtava["tehty"] else "[ ]"
        print(f"{i}. {tila} {tehtava['kuvaus']}")

    try:
        numero = int(input("\nAnna tehtävän numero: "))
    except ValueError:
        print("Virheellinen numero.")
        odota_enter()
        return

    if numero < 1 or numero > len(tasks):
        print("Virheellinen tehtävän numero.")
        odota_enter()
        return

    tehtava = tasks[numero - 1]
    tehtava["tehty"] = not tehtava["tehty"]

    if tehtava["tehty"]:
        kirjoita_loki(
            f"Tehtävä '{tehtava['kuvaus']}' merkitty tehdyksi."
        )
        print("Tehtävä merkitty tehdyksi.")
    else:
        kirjoita_loki(
            f"Tehtävä '{tehtava['kuvaus']}' merkitty tekemättömäksi."
        )
        print("Tehtävä merkitty tekemättömäksi.")

    odota_enter()


def poista_tehtava(tasks):
    otsikko("POISTA TEHTÄVÄ")

    if not tasks:
        print("Ei tehtäviä.")
        odota_enter()
        return

    for i, tehtava in enumerate(tasks, start=1):
        print(f"{i}. {tehtava['kuvaus']}")

    try:
        numero = int(input("\nAnna poistettavan tehtävän numero: "))
    except ValueError:
        print("Virheellinen numero.")
        odota_enter()
        return

    if numero < 1 or numero > len(tasks):
        print("Virheellinen tehtävän numero.")
        odota_enter()
        return

    tehtava = tasks[numero - 1]

    vahvistus = input(
        f"Poistetaanko tehtävä '{tehtava['kuvaus']}'? (K/E): "
    ).strip().lower()

    if vahvistus == "k":
        poistettu = tasks.pop(numero - 1)

        kirjoita_loki(
            f"Poistettiin tehtävä: '{poistettu['kuvaus']}'"
        )

        print("Tehtävä poistettu.")
    else:
        print("Poisto peruttu.")

    odota_enter()


def muokkaa_tehtavaa(tasks):
    otsikko("MUOKKAA TEHTÄVÄÄ")

    if not tasks:
        print("Ei tehtäviä.")
        odota_enter()
        return

    for i, tehtava in enumerate(tasks, start=1):
        print(f"{i}. {tehtava['kuvaus']}")

    try:
        numero = int(input("\nAnna muokattavan tehtävän numero: "))
    except ValueError:
        print("Virheellinen numero.")
        odota_enter()
        return

    if numero < 1 or numero > len(tasks):
        print("Virheellinen tehtävän numero.")
        odota_enter()
        return

    tehtava = tasks[numero - 1]

    print("\nJätä kenttä tyhjäksi, jos et halua muuttaa sitä.")

    uusi_kuvaus = input(
        f"Uusi kuvaus [{tehtava['kuvaus']}]: "
    ).strip()

    if uusi_kuvaus:
        vanha_kuvaus = tehtava["kuvaus"]
        tehtava["kuvaus"] = uusi_kuvaus

        kirjoita_loki(
            f"Muokattiin tehtävän kuvaus: "
            f"'{vanha_kuvaus}' -> '{uusi_kuvaus}'"
        )

    while True:
        nykyinen_prioriteetti = tehtava.get("prioriteetti", 2)

        uusi_prioriteetti = input(
            f"Uusi prioriteetti [{nykyinen_prioriteetti}] "
            "(1-3, Enter = ei muutosta): "
        ).strip()

        if not uusi_prioriteetti:
            break

        if uusi_prioriteetti in ("1", "2", "3"):
            tehtava["prioriteetti"] = int(uusi_prioriteetti)
            break

        print("Virheellinen valinta. Anna numero 1, 2 tai 3.")

    nykyinen_deadline = tehtava.get("deadline", "")

    if nykyinen_deadline:
        deadline_naytto = nykyinen_deadline
    else:
        deadline_naytto = "ei määräpäivää"

    while True:
        uusi_deadline = input(
            f"Uusi määräpäivä [{deadline_naytto}] "
            "(Enter = ei muutosta, - = tyhjennä): "
        ).strip()

        if not uusi_deadline:
            break

        if uusi_deadline == "-":
            tehtava["deadline"] = ""
            break

        try:
            datetime.strptime(uusi_deadline, "%Y-%m-%d")
            tehtava["deadline"] = uusi_deadline
            break
        except ValueError:
            print("Virheellinen päivämäärä. Käytä muotoa YYYY-MM-DD.")

    print("\nTehtävä muokattu.")
    odota_enter()


def nayta_tekemattomat(tasks):
    otsikko("TEKEMÄTTÖMÄT TEHTÄVÄT")

    tekemattomat = [
        tehtava for tehtava in tasks
        if not tehtava["tehty"]
    ]

    if not tekemattomat:
        print("Ei tekemättömiä tehtäviä.")
        odota_enter()
        return

    for i, tehtava in enumerate(tekemattomat, start=1):
        print(f"{i}. [ ] {tehtava['kuvaus']}")

    odota_enter()


def nayta_tehdyt(tasks):
    otsikko("TEHDYT TEHTÄVÄT")

    tehdyt = [
        tehtava for tehtava in tasks
        if tehtava["tehty"]
    ]

    if not tehdyt:
        print("Ei tehtyjä tehtäviä.")
        odota_enter()
        return

    for i, tehtava in enumerate(tehdyt, start=1):
        print(f"{i}. [x] {tehtava['kuvaus']}")

    odota_enter()


def hae_tehtavia(tasks):
    otsikko("HAE TEHTÄVIÄ")

    hakusana = input("Anna hakusana: ").strip().lower()

    tulokset = [
        tehtava for tehtava in tasks
        if hakusana in tehtava["kuvaus"].lower()
    ]

    if not tulokset:
        print("Hakusanalla ei löytynyt tehtäviä.")
        odota_enter()
        return

    print("\nHakutulokset:")

    for i, tehtava in enumerate(tulokset, start=1):
        tila = "[x]" if tehtava["tehty"] else "[ ]"
        print(f"{i}. {tila} {tehtava['kuvaus']}")

    odota_enter()


def nayta_tilastot(tasks):
    otsikko("TILASTOT")

    maara = len(tasks)
    tehdyt = sum(1 for tehtava in tasks if tehtava["tehty"])
    tekemattomat = maara - tehdyt
    korkeat = sum(
        1 for tehtava in tasks
        if tehtava.get("prioriteetti", 2) == 3
    )

    if maara > 0:
        prosentti = tehdyt / maara * 100
    else:
        prosentti = 0

    print(f"Tehtäviä yhteensä: {maara}")
    print(f"Tehtyjä: {tehdyt}")
    print(f"Tekemättömiä: {tekemattomat}")
    print(f"Korkean prioriteetin tehtäviä: {korkeat}")
    print(f"Valmiusaste: {prosentti:.1f} %")

    odota_enter()