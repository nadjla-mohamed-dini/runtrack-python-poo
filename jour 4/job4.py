class Forme:
    def __init__(self):
        pass
    def aire():
        return 0

class Rectangle (Forme):
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        Forme.__init__(self)
    def aire(self):
        return self.largeur * self.hauteur 

rec = Rectangle(5,19)
print(rec.aire())
rec2 = Rectangle(4,55)
rec3 = Rectangle(11,44)
print(rec2.aire())
print(rec3.aire())