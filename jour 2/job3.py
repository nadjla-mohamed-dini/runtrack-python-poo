class Livre:
    def __init__(self,titre,autrice,nombre_page,disponible = True ):
        self.__titre = titre
        self.__autrice = autrice
        self.__nombre_page = nombre_page
        self.__disponible = disponible
        #getters
    def get_titre(self):
        return self.__titre
    def get_autrice(self):
        return self.__autrice
    def get_nombre_page(self):
        return self.__nombre_page
    #setters
    def set_titre(self,titre):
        self.__titre = titre
    def set_autrice(self,autrice):
        self.__autrice = autrice
    def set_nombre_page(self,nombre_page):
        if isinstance(nombre_page,int) and nombre_page >0:
            self.__nombre_page = nombre_page
        else:
            print("Erreur choisir un nombre de page")
    def verification(self):
        return self.__disponible
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"le livre {self.__titre} a été emprunter")
        else:
            print(f"le livre {self.__titre}n'est pas disponible")
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"le livre {self.__titre}a été rendu")
        else:
            print(f"le livre {self.__titre} est disponible")


bouquin = Livre("Les morsures du passé","Lisa Gardner",412,True)
print(bouquin.verification())
bouquin.emprunter()
bouquin.emprunter()
bouquin.rendre()
print(bouquin.verification())