class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    def veillir(self):
        self.age +=1
    def nommer(self):
        self.prenom = "Oreo"


animal = Animal()
print(f"l'age de l'animal {animal.age} ans ")
animal.veillir()
print(f"l'age de l'animal {animal.age} ans  ")
animal.nommer()
print(f"l'animal se nomme {animal.prenom}")