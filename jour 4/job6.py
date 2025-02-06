class Vehicule:
    def __init__(self,marque,modele,année,prix):
        self.marque = marque
        self.modele = modele
        self.année = année 
        self.prix = prix
        
    def informationsVehicule(self):
        print (f"Infos du vehicle: \n"
        f"Marque: {self.marque}\n"
        f"Modele: {self.modele}\n"
        f"Année: {self.année}\n"
        f"Prix: {self.prix} €\n")
    
    def demarrer(self):
        print("Attend je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, année, prix):
        super().__init__(marque, modele, année, prix)
        self.porte = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.porte}")
    
    def demarrer(self):
        print("VROOOOOM.La voiture demarre")

class Moto(Vehicule):
    def __init__(self, marque, modele, année, prix):
         super().__init__(marque, modele, année, prix)
    def demarrer(self):
        print("BRRRR.La moto BRRRR")
     


caisse = Voiture("Mercedes","Classe A", 2020, 18500)
caisse.informationsVehicule()
caisse.demarrer()
motard = Moto("Yamaha", "MT_07", 2021, 8000)
motard.demarrer()

    
    
