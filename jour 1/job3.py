class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def addition (self):
        resultat = self.nombre1 + self.nombre2
        return f" Le resultat est: {resultat}"

valeur = Operation(12,7)
print(valeur.addition())