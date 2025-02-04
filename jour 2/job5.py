class Voiture:
    def __init__(self,marque,modele,année,kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__année = année
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50
    
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_année(self):
        return self.__année
    def get_kilometrage(self):
        return self.__kilometrage
    def get_en_marche(self):
        return self.__en_marche
    
    def set_marque(self,marque):
        self.__marque = marque
    def set_modele(self,modele):
        self.__modele = modele
    def set_année(self,année):
        self.__année = année
    def set_kilometrage(self,kilometrage):
        self.__kilometrage = kilometrage
    def set_en_marche(self,en_marche):
        self.__en_marche = en_marche

    

    def demarrer(self):
        if self.__verifier_plein()> 30:
            self.__en_marche = True
            print("la voiture démarre")
        else:
            print("la voiture ne peut pas démarrer")
    
    def arreter(self):
        self.__en_marche = False
        print("la voiture a été arreter")

    def __verifier_plein(self):
        return self.__reservoir

caisse = Voiture("BMW","SUV","2023","2000 km")
print(caisse.get_année())
print(caisse.get_modele())
print(caisse.get_marque())
print(caisse.get_kilometrage())
print(caisse.get_en_marche())
caisse.demarrer()
caisse.arreter()
caisse.set_année(1999)
caisse.set_marque("Fiat 500")
print(caisse.get_marque())
print(caisse.get_année())
