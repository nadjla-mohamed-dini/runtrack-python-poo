class Rectangle:
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur
    
    def perimetre(self):
        return self.__largeur + self.__largeur * 2
    
    def surface(self):
        return self.__longeur * self.__largeur
    
    def get_longeur(self):
        return self.__longeur
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self,largeur):
        self.__largeur = largeur 
    def set_longeur(self,longeur):
        self.__longeur = longeur 

class Parallepipede (Rectangle):
    def __init__(self,hauteur):
        self.hauteur = hauteur
        Rectangle.__init__(self,longeur=22, largeur=8)
    def volume(self,):
        return self.longeur * self.largeur * self.hauteur


rectangle = Rectangle(18,5)
print(rectangle.get_largeur())
print(rectangle.get_longeur())
rectangle.set_largeur(10)
rectangle.set_longeur(25)
print(rectangle.get_largeur())
print(rectangle.get_longeur())
print(rectangle.perimetre())
print(rectangle.surface())

parallepipede = Parallepipede(7)
print(parallepipede.get_largeur())
print(parallepipede.get_longeur())
print(parallepipede.perimetre())
print(parallepipede.surface())
print(parallepipede.volume())
