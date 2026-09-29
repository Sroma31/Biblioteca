from libro import Libro
from libreria import Libreria


def leggi_numero(messaggio):
    while True:
        valore = input(messaggio).strip()
        try:
            return int(valore)
        except ValueError:
            print("Devi inserire un numero.")


def aggiungi(libreria):
    autore = input("Autore: ").strip()
    titolo = input("Titolo: ").strip()
    anno = leggi_numero("Anno: ")
    editore = input("Editore: ").strip()
    pagine = leggi_numero("Pagine: ")

    if not all([autore, titolo, editore]):
        print("Autore, titolo e editore sono obbligatori.")
        return

    libro = Libro(autore, titolo, anno, editore, pagine)
    libreria.aggiungi(libro)
    print("Libro aggiunto.")


def cerca(libreria):
    parola = input("Cerca per autore o titolo: ").strip()
    trovati = libreria.cerca(parola)
    if not trovati:
        print("Nessun libro trovato.")
    else:
        for libro in trovati:
            print(libro)


def elimina(libreria):
    libreria.elenca()
    if not libreria.libri:
        return
    n = leggi_numero("Numero del libro da eliminare: ") - 1
    if libreria.elimina(n):
        print("Libro eliminato.")
    else:
        print("Numero non valido.")


def menu():
    libreria = Libreria()
    while True:
        print("\n--- Biblioteca ---")
        print("1. Aggiungi libro")
        print("2. Elenca libri")
        print("3. Cerca libro")
        print("4. Elimina libro")
        print("5. Esci")
        scelta = input("Scegli: ").strip()

        if scelta == "1":
            aggiungi(libreria)
        elif scelta == "2":
            libreria.elenca()
        elif scelta == "3":
            cerca(libreria)
        elif scelta == "4":
            elimina(libreria)
        elif scelta == "5":
            break
        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    menu()


























