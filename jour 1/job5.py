class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def AfficherLesPoints(self):
        afficher = self.x, self.y
        return f"points: {afficher}"
    
    def afficherX(self):
        afficher_x = self.x
        return f"point x: {afficher_x}"
    
    def afficherY(self):
        afficher_y = self.y
        return f"point y: {afficher_y}"
    def changerX(self):
        changer_x = self.x
        return f"nouveau point x: {changer_x}"
    def changerY(self):
        changer_y = self.y
        return f"nouveau point y: {changer_y}"
    
valeur = Point(2,7)
print(valeur.AfficherLesPoints())
print(valeur.afficherX())
print(valeur.afficherY())
valeur = Point(5,4)
print(valeur.changerX())
print(valeur.changerY())
