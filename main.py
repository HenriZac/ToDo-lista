from tasks import (
    otsikko,
    nayta_tehtavat,
    lisaa_tehtava,
    merkitse_tehtava,
    poista_tehtava,
    muokkaa_tehtavaa,
    nayta_tekemattomat,
    nayta_tehdyt,
    hae_tehtavia,
    nayta_tilastot
)

from storage import (
    load_tasks,
    save_tasks
)


def nayta_paavalikko(tehtavat):
    otsikko("TEHTAVALISTA")

    tekemattomat = sum(
        1
        for tehtava in tehtavat
        if not tehtava["tehty"]
    )

    tehdyt = sum(
        1
        for tehtava in tehtavat
        if tehtava["tehty"]
    )

    print(
        f"Tehtavia: {len(tehtavat)}"
    )

    print(
        f"Tekemattomia: {tekemattomat}"
    )

    print(
        f"Tehtyja: {tehdyt}"
    )

    print()
    print("==============================")
    print("1. Nayta tehtavat")
    print("2. Lisaa tehtava")
    print("3. Merkitse tehtava tehdyksi")
    print("4. Muokkaa tehtavaa")
    print("5. Poista tehtava")
    print("6. Nayta tekemattomat")
    print("7. Nayta tehdyt")
    print("8. Hae tehtavia")
    print("9. Tilastot")
    print("10. Tallenna ja lopeta")
    print("==============================")


def main():
    tehtavat = load_tasks()

    while True:

        nayta_paavalikko(tehtavat)

        valinta = input(
            "\nValitse toiminto: "
        ).strip()

        if valinta == "1":
            nayta_tehtavat(tehtavat)

        elif valinta == "2":
            lisaa_tehtava(tehtavat)
            save_tasks(tehtavat)

        elif valinta == "3":
            merkitse_tehtava(tehtavat)
            save_tasks(tehtavat)

        elif valinta == "4":
            muokkaa_tehtavaa(tehtavat)
            save_tasks(tehtavat)

        elif valinta == "5":
            poista_tehtava(tehtavat)
            save_tasks(tehtavat)

        elif valinta == "6":
            nayta_tekemattomat(tehtavat)

        elif valinta == "7":
            nayta_tehdyt(tehtavat)

        elif valinta == "8":
            hae_tehtavia(tehtavat)

        elif valinta == "9":
            nayta_tilastot(tehtavat)

        elif valinta == "10":
            save_tasks(tehtavat)

            otsikko("OHJELMA LOPETETAAN")

            print(
                "Tehtavat tallennettu."
            )

            print(
                "Kiitos ohjelman kayttamisesta!"
            )

            break

        else:
            print(
                "\nVirheellinen valinta."
            )

            input(
                "Paina Enter ja yrita uudelleen..."
            )


if __name__ == "__main__":
    main()