from loki import kirjoita_loki
from datetime import datetime

def tyhjenna_naytto():
    print("\n" * 40)


def odota_enter():
    input("\nPaina Enter palataksesi takaisin...")


def otsikko(teksti):
    tyhjenna_naytto()

    print("=" * 40)
    print(f"{teksti:^40}")
    print("=" * 40)
    print()


def nayta_tehtavat(tehtavat):
    otsikko("KAIKKI TEHTAVAT")

    if not tehtavat:
        print("Ei tehtavia.")
        odota_enter()
        return

    for numero, tehtava in enumerate(tehtavat, start=1):

        if tehtava["tehty"]:
            status = "x"
        else:
            status = " "

        prioriteetti = tehtava.get(
            "prioriteetti",
            "normaali"
        )

        deadline = tehtava.get(
            "deadline",
            ""
        )

        print(
            f"{numero}. [{status}] "
            f"{tehtava['kuvaus']}"
        )

        print(
            f"    Prioriteetti: {prioriteetti}"
        )

        if deadline:
            print(
                f"    Deadline: {deadline}"
            )

        print()

    odota_enter()


def lisaa_tehtava(tehtavat):
    otsikko("LISAA TEHTAVA")

    kuvaus = input(
        "Anna uuden tehtavan kuvaus:\n> "
    ).strip()

    if not kuvaus:
        print("\nVirhe: kuvaus ei voi olla tyhja.")
        odota_enter()
        return

    print("\nPrioriteetti")
    print("----------------")
    print("1. Matala")
    print("2. Normaali")
    print("3. Korkea")

    valinta = input(
        "\nValitse prioriteetti: "
    ).strip()

    if valinta == "1":
        prioriteetti = "matala"

    elif valinta == "3":
        prioriteetti = "korkea"

    else:
        prioriteetti = "normaali"

    print()

    deadline = input(
        "Anna deadline muodossa VVVV-KK-PP\n"
        "(tai paina Enter jos ei ole deadlinea):\n> "
    ).strip()

    if deadline:
        try:
            datetime.strptime(
                deadline,
                "%Y-%m-%d"
            )

        except ValueError:
            print("\nVirheellinen paivamaara.")
            print("Kayta muotoa VVVV-KK-PP.")
            odota_enter()
            return

    uusi_tehtava = {
        "kuvaus": kuvaus,
        "tehty": False,
        "prioriteetti": prioriteetti,
        "deadline": deadline
    }

    tehtavat.append(uusi_tehtava)

    kirjoita_loki(
        f"Lisattiin tehtava: '{kuvaus}'"
    )

    print()
    print("Tehtava lisatty onnistuneesti!")

    odota_enter()


def merkitse_tehtava(tehtavat):
    otsikko("MERKITSE TEHTAVA TEHDYKSI")

    if not tehtavat:
        print("Ei tehtavia.")
        odota_enter()
        return

    for numero, tehtava in enumerate(
        tehtavat,
        start=1
    ):
        if tehtava["tehty"]:
            status = "x"
        else:
            status = " "

        print(
            f"{numero}. [{status}] "
            f"{tehtava['kuvaus']}"
        )

    print()

    try:
        numero = int(
            input(
                "Anna tehtavan numero:\n> "
            )
        )

        if numero < 1 or numero > len(tehtavat):
            print("\nVirhe: tehtavaa ei loydy.")
            odota_enter()
            return

        tehtava = tehtavat[numero - 1]

        tehtava["tehty"] = not tehtava["tehty"]

        if tehtava["tehty"]:
            kirjoita_loki(
                f"Tehtava merkitty tehdyksi: "
                f"'{tehtava['kuvaus']}'"
            )

            print(
                f"\n'{tehtava['kuvaus']}' "
                "merkitty tehdyksi."
            )

        else:
            kirjoita_loki(
                f"Tehtava merkitty tekemattomaksi: "
                f"'{tehtava['kuvaus']}'"
            )

            print(
                f"\n'{tehtava['kuvaus']}' "
                "merkitty tekemattomaksi."
            )

    except ValueError:
        print("\nVirhe: anna kelvollinen numero.")

    odota_enter()


def poista_tehtava(tehtavat):
    otsikko("POISTA TEHTAVA")

    if not tehtavat:
        print("Ei tehtavia.")
        odota_enter()
        return

    for numero, tehtava in enumerate(
        tehtavat,
        start=1
    ):
        print(
            f"{numero}. {tehtava['kuvaus']}"
        )

    print()

    try:
        numero = int(
            input(
                "Anna poistettavan tehtavan numero:\n> "
            )
        )

        if numero < 1 or numero > len(tehtavat):
            print("\nVirhe: tehtavaa ei loydy.")
            odota_enter()
            return

        tehtava = tehtavat[numero - 1]

        print()
        print(
            f"Poistetaanko tehtava "
            f"'{tehtava['kuvaus']}'?"
        )

        vahvistus = input(
            "Kirjoita K vahvistaaksesi: "
        ).strip().lower()

        if vahvistus == "k":
            poistettu = tehtavat.pop(
                numero - 1
            )

            kirjoita_loki(
                f"Poistettiin tehtava: "
                f"'{poistettu['kuvaus']}'"
            )

            print("\nTehtava poistettu.")

        else:
            print("\nPoisto peruttu.")

    except ValueError:
        print("\nVirhe: anna kelvollinen numero.")

    odota_enter()


def muokkaa_tehtavaa(tehtavat):
    otsikko("MUOKKAA TEHTAVAA")

    if not tehtavat:
        print("Ei tehtavia.")
        odota_enter()
        return

    for numero, tehtava in enumerate(
        tehtavat,
        start=1
    ):
        print(
            f"{numero}. "
            f"{tehtava['kuvaus']}"
        )

    print()

    try:
        numero = int(
            input(
                "Anna muokattavan tehtavan numero:\n> "
            )
        )

        if numero < 1 or numero > len(tehtavat):
            print("\nVirhe: tehtavaa ei loydy.")
            odota_enter()
            return

        tehtava = tehtavat[numero - 1]

        vanha_kuvaus = tehtava["kuvaus"]
        vanha_prioriteetti = tehtava.get(
            "prioriteetti",
            "normaali"
        )
        vanha_deadline = tehtava.get(
            "deadline",
            ""
        )

        print()
        print(
            f"Nykyinen kuvaus: "
            f"{vanha_kuvaus}"
        )

        uusi_kuvaus = input(
            "Uusi kuvaus "
            "(Enter = ei muutosta):\n> "
        ).strip()

        if uusi_kuvaus:
            tehtava["kuvaus"] = uusi_kuvaus

        print()
        print(
            "Nykyinen prioriteetti:",
            vanha_prioriteetti
        )

        print()
        print("1. Matala")
        print("2. Normaali")
        print("3. Korkea")
        print("Enter = ei muutosta")

        prioriteetti = input(
            "Valinta: "
        ).strip()

        if prioriteetti == "1":
            tehtava["prioriteetti"] = "matala"

        elif prioriteetti == "2":
            tehtava["prioriteetti"] = "normaali"

        elif prioriteetti == "3":
            tehtava["prioriteetti"] = "korkea"

        print()
        print(
            "Nykyinen deadline:",
            vanha_deadline
        )

        uusi_deadline = input(
            "Uusi deadline "
            "(Enter = ei muutosta):\n> "
        ).strip()

        if uusi_deadline:
            try:
                datetime.strptime(
                    uusi_deadline,
                    "%Y-%m-%d"
                )

                tehtava["deadline"] = uusi_deadline

            except ValueError:
                print(
                    "\nVirheellinen paivamaara."
                )

                print(
                    "Deadlinea ei muutettu."
                )

        kirjoita_loki(
            f"Muokattiin tehtavaa: "
            f"'{vanha_kuvaus}' -> "
            f"'{tehtava['kuvaus']}'"
        )

        print("\nTehtava paivitetty.")

    except ValueError:
        print("\nVirhe: anna kelvollinen numero.")

    odota_enter()


def nayta_tekemattomat(tehtavat):
    otsikko("TEKEMATTOMAT TEHTAVAT")

    tekemattomat = [
        tehtava
        for tehtava in tehtavat
        if not tehtava["tehty"]
    ]

    if not tekemattomat:
        print("Kaikki tehtavat on tehty!")
        odota_enter()
        return

    for numero, tehtava in enumerate(
        tekemattomat,
        start=1
    ):
        print(
            f"{numero}. [ ] "
            f"{tehtava['kuvaus']}"
        )

        print(
            f"    Prioriteetti: "
            f"{tehtava.get('prioriteetti', 'normaali')}"
        )

        if tehtava.get("deadline"):
            print(
                f"    Deadline: "
                f"{tehtava['deadline']}"
            )

        print()

    odota_enter()


def nayta_tehdyt(tehtavat):
    otsikko("TEHDYT TEHTAVAT")

    tehdyt = [
        tehtava
        for tehtava in tehtavat
        if tehtava["tehty"]
    ]

    if not tehdyt:
        print("Yhtaan tehtavaa ei ole tehty.")
        odota_enter()
        return

    for numero, tehtava in enumerate(
        tehdyt,
        start=1
    ):
        print(
            f"{numero}. [x] "
            f"{tehtava['kuvaus']}"
        )

        print()

    odota_enter()


def hae_tehtavia(tehtavat):
    otsikko("HAE TEHTAVIA")

    hakusana = input(
        "Anna hakusana:\n> "
    ).strip().lower()

    if not hakusana:
        print("\nHakusana ei voi olla tyhja.")
        odota_enter()
        return

    tulokset = [
        tehtava
        for tehtava in tehtavat
        if hakusana in tehtava["kuvaus"].lower()
    ]

    if not tulokset:
        print("\nTehtavia ei loytynyt.")
        odota_enter()
        return

    print(
        f"\nLoytyi {len(tulokset)} tehtavaa:\n"
    )

    for numero, tehtava in enumerate(
        tulokset,
        start=1
    ):
        status = "x" if tehtava["tehty"] else " "

        print(
            f"{numero}. [{status}] "
            f"{tehtava['kuvaus']}"
        )

        print(
            f"    Prioriteetti: "
            f"{tehtava.get('prioriteetti', 'normaali')}"
        )

        if tehtava.get("deadline"):
            print(
                f"    Deadline: "
                f"{tehtava['deadline']}"
            )

        print()

    odota_enter()


def nayta_tilastot(tehtavat):
    otsikko("TILASTOT")

    yhteensa = len(tehtavat)

    tehdyt = sum(
        1
        for tehtava in tehtavat
        if tehtava["tehty"]
    )

    tekemattomat = yhteensa - tehdyt

    korkeat = sum(
        1
        for tehtava in tehtavat
        if tehtava.get("prioriteetti")
        == "korkea"
    )

    print(
        f"Tehtavia yhteensa:    {yhteensa}"
    )

    print(
        f"Tehtyja tehtavia:     {tehdyt}"
    )

    print(
        f"Tekemattomia:         {tekemattomat}"
    )

    print(
        f"Korkean prioriteetin: {korkeat}"
    )

    if yhteensa > 0:
        prosentti = (
            tehdyt / yhteensa
        ) * 100

        print(
            f"\nValmiusaste:          "
            f"{prosentti:.1f} %"
        )

    else:
        print(
            "\nValmiusaste:          0 %"
        )

    odota_enter()