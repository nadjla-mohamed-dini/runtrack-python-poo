class Personne:
    def __init__(self,age = 14):
        self.age = age
         

    def afficherAge(self):
        afficher = self.age
        print(f'Age: {afficher} ans')
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self,nouvel_age):
        if isinstance(nouvel_age,int):
            self.age = nouvel_age

class Eleve (Personne): 
    def __init__(self):
        Personne.__init__(self)

    
    def allerEnCour(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans") 
    
class Professeur (Personne):
    def __init__(self, matiereEnseigner):
        self.__matiereEnseigner = matiereEnseigner
        Personne.__init__(self,age = 40)
    def enseigner(self):
        print("Le cours va commencer")

eleve = Eleve()
eleve.afficherAge()
eleve.bonjour()
eleve.allerEnCour()
eleve.modifierAge(15)
eleve.afficherAge()
#Objet prof 40 ans qui dit hello le cours va commencer
prof = Professeur("Mathématiques")
prof.afficherAge()
prof.bonjour()
prof.enseigner()
