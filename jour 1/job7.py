class Personnage:
    #constructeur
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def gauche(self):
        self.x -= 1
        return f'le personnage se deplace vers la gauche, nouvelle position: {self.x}'
    
    def droite(self):
        self.x += 1
        return f'le personnage se déplace vers la doite, nouvelle position: {self.x}'

    def haut(self):
        self.x += 1
        return f'le personnage se deplace vers le haut, nouvelle position: {self.y}'
    def bas(self):
        self.y -=1
        return f'le personnage se deplace vers le bas, nouvelle position: {self.y}'
    def position(self):
        return (self.x, self.y)

mouvement = Personnage(-4,7)
print(mouvement.gauche())
print(mouvement.droite())
print(mouvement.haut())
print(mouvement.bas())
print(mouvement.position())