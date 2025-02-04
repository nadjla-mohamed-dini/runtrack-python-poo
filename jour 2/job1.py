class Rectangle:
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur
    
    def set_longeur(self,longeur):
         self.__longeur = longeur
    #modifier la largeur et la longeur 
    def set_largeur(self,largeur):
         self._largeur = largeur 
    
    def get_longeur(self):
        return self.__longeur   
    def get_largeur(self):
        return self.__largeur

rec = Rectangle(10,5)
print(rec.get_largeur())
print(rec.get_longeur())

#modifie les valeurs 
rec.set_largeur(10)
rec.set_longeur(21)
print(rec.get_longeur())
print(rec.get_largeur())

