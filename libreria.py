from libro import Libro


class Libreria:
    def __init__(self):
        self.libri = []

    def aggiungi(self, libro):
        self.libri.append(libro)

    def elenca(self):
        if not self.libri:
            print("Nessun libro presente.")
            return
        for i, libro in enumerate(self.libri, 1):
            print(f"{i}. {libro}")

    

    def cerca(self, parola):
        parola = parola.lower()
        return [
            libro for libro in self.libri
            if parola in libro.autore.lower() or parola in libro.titolo.lower()
        ]

    def conta(self):
        return len(self.libri)

    
    def elimina(self, indice):
        if 0 <= indice < len(self.libri):
            self.libri.pop(indice)
            return True
        return False

    