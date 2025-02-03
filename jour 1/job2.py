class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

valeur = Operation(12,3)
print(f"le nombre1 est {valeur.nombre1}")
print(f"le nombre2 est {valeur.nombre2}")