from storage import load_tasks, save_tasks
from tasks import (
    nayta_tehtavat,
    lisaa_tehtava,
    merkitse_tehtava,
    poista_tehtava,
    muokkaa_tehtavaa,
    nayta_tekemattomat,
    nayta_tehdyt,
    hae_tehtavia,
    nayta_tilastot,
    otsikko
)


def main():
    tehtavat = load_tasks()

    while True:
        otsikko("TEHTÄVÄLISTA")

        print("1. Näytä kaikki tehtävät")
        print("2. Lisää tehtävä")
        print("3. Merkitse tehtävä tehdyksi / tekemättömäksi")
        print("4. Muokkaa tehtävää")
        print("5. Poista tehtävä")
        print("6. Näytä tekemättömät")
        print("7. Näytä tehdyt")
        print("8. Hae tehtäviä")
        print("9. Näytä tilastot")
        print("10. Tallenna ja lopeta")

        valinta = input("\nValitse toiminto: ").strip()

        if valinta == "1":
            nayta_tehtavat(tehtavat)

        elif valinta == "2":
            lisaa_tehtava(tehtavat)

            onnistui = save_tasks(tehtavat)

            if not onnistui:
                print("Varoitus: tehtävän tallennus epäonnistui.")

        elif valinta == "3":
            merkitse_tehtava(tehtavat)

            onnistui = save_tasks(tehtavat)

            if not onnistui:
                print("Varoitus: muutoksen tallennus epäonnistui.")

        elif valinta == "4":
            muokkaa_tehtavaa(tehtavat)

            onnistui = save_tasks(tehtavat)

            if not onnistui:
                print("Varoitus: muutoksen tallennus epäonnistui.")

        elif valinta == "5":
            poista_tehtava(tehtavat)

            onnistui = save_tasks(tehtavat)

            if not onnistui:
                print("Varoitus: muutoksen tallennus epäonnistui.")

        elif valinta == "6":
            nayta_tekemattomat(tehtavat)

        elif valinta == "7":
            nayta_tehdyt(tehtavat)

        elif valinta == "8":
            hae_tehtavia(tehtavat)

        elif valinta == "9":
            nayta_tilastot(tehtavat)

        elif valinta == "10":
            onnistui = save_tasks(tehtavat)

            if onnistui:
                print("Tehtävät tallennettu. Ohjelma lopetetaan.")
            else:
                print(
                    "Tehtävien tallennus epäonnistui. "
                    "Ohjelma lopetetaan."
                )

            break

        else:
            print("Virheellinen valinta.")
            input("Paina Enter jatkaaksesi...")


if __name__ == "__main__":
    main()