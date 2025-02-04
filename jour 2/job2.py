class Livre:
    def __init__(self,titre,autrice,nombre_page):
        self.__titre = titre
        self.__autrice = autrice
        self.__nombre_page = nombre_page
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

bouquin = Livre("Les morsures du passé","Lisa Gardner",412)
print(bouquin.get_autrice())
print(bouquin.get_titre())
print(bouquin.get_nombre_page())
bouquin.set_nombre_page(27)
print(bouquin.get_nombre_page())
