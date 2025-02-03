class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA /100)

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT/ {self.prixHT}, TVA: {self.TVA}%"


    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA


produit1 = Produit("Produit A", 120, 20)
produit2 = Produit("Produit B", 248, 10)
produit3 = Produit("Produit C", 333, 5)


print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())


produit1.modifierNom("Nouveau Produit A")
produit1.modifierPrix(176)
produit2.modifierNom("Nouveau Produit B")
produit2.modifierPrix(220)
produit3.modifierNom("Nouveau Produit C")
produit3.modifierPrix(180)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())
