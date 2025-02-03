class Personne:
    def __init__(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter (self):
        return f"Je suis {self.prenom} {self.nom}"
    
p1 = Personne("Jake", "Peralta")
p2 = Personne("Sheldon","Cooper")
p3 = Personne("Harvey","Specter")
print(p1.SePresenter())
print(p2.SePresenter())
print(p3.SePresenter())