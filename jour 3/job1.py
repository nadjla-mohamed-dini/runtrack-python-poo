class Ville:
    def __init__(self,nom,nbr_habitants):
        self.__nom = nom
        self.__nbr_habitants = nbr_habitants

    def get_nom(self):
        return self.__nom
    
    def get_nbr_habitants(self):
        return self.__nbr_habitants
    
    def set_nbr_habitant(self,nombre):
        self.__nbr_habitants = nombre
    

class Personne:
    def __init__(self,nom,age,ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    def ajouter_Population(self,):
        habitant = self.__ville.get_nbr_habitants()

        self.__ville.set_nbr_habitant(habitant + 1)
        print(f"Mise a jour de la population de la ville de {self.__ville.get_nom()}: {self.__ville.get_nbr_habitants()}")

paris = Ville("Paris",1000000)
print(f"Population de la ville de {paris.get_nom()}: {paris.get_nbr_habitants()}")
marseille = Ville("Marseille",861635)
print(f"Population de la ville de{marseille.get_nom()}: {marseille.get_nbr_habitants()}")

john = Personne("John",45, paris)
myrtille = Personne("Myrtille",4, paris)
chloe = Personne("Chloe",18, marseille)

john.ajouter_Population()
myrtille.ajouter_Population()
chloe.ajouter_Population()
print(f"Mise a jour de la poulation de {paris.get_nom()}: {paris.get_nbr_habitants()}")
print(f"Mise a jour de la population de {marseille.get_nom()}: {marseille.get_nbr_habitants()}")