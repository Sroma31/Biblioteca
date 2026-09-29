class Libro:
    def __init__(self, autore, titolo, anno, editore, pagine):
        self.autore = autore
        self.titolo = titolo
        self.anno = anno
        self.editore = editore
        self.pagine = pagine

    def readingTime(self):
        # Assuming an average reading speed of 1 page per minute
        return self.pagine
    

    def __str__(self):
        return f"{self.titolo} - {self.autore} ({self.anno}) - {self.editore} - {self.pagine} pagine"
