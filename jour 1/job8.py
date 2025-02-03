import math

class Cercle: 
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
        return f'Le rayon du cercle a changé : {self.rayon}'

    def afficherInfos(self):
        circonference = self.circonference()
        aire = self.aire()
        diametre = self.diametre()
        return f'Voici les infos du cercle : Circonférence = {circonference}, Aire = {aire}, Diamètre = {diametre}, Rayon = {self.rayon}'

    def circonference(self):
        return math.pi * self.diametre()
    
    def aire(self):
        return math.pi * (self.rayon ** 2)
    
    def diametre(self):
        return 2 * self.rayon

rond = Cercle(3)

print(rond.changerRayon(4))
print(rond.afficherInfos())
print(f"L'aire du cercle est de {rond.aire()}")
print(f"La circonférence du cercle est de {rond.circonference()}")
print(f"Le diamètre du cercle est de {rond.diametre()}")

rond = Cercle(1)
print(rond.changerRayon(7))
print(rond.afficherInfos())
print(f"L'aire du cercle est de {rond.aire()}")
print(f"La circonférence du cercle est de {rond.circonference()}")
print(f"Le diamètre du cercle est de {rond.diametre()}")