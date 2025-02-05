class CompteBancaire:
    def __init__(self,numero_de_compte,nom,prenom,solde,decouvert = False):
        self.__numero_de_compte = numero_de_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde =solde
        self.__decouvert = decouvert
    def get_solde(self):
         return self.__solde
    def afficher(self):
        numero_de_compte = self.__numero_de_compte
        nom = self.__nom
        prenom = self.__prenom
        solde = self.__solde
        decouvert = self.__decouvert
        return (f"Les infos du compte bancaire:\n"
                f"prenom: {prenom}\n"
                f"nom: {nom}\n"
                f"numero de compte: {numero_de_compte} \n"
                f"solde: {solde}\n"
                f"Découvert autorisé: {"Oui" if self.__decouvert else "Non"}")
    
    def afficherSolde(self):
        print(f"Le solde de {self.__nom} est de {self.__solde} €")

    def set_versement(self,montant_versement):
        if montant_versement >0:
            self.__solde += montant_versement
            print(f"Versement de {montant_versement}€ effectuer, nouveau solde {self.__solde}€")

    def retrait(self,montant_retrait):
        if montant_retrait >0:
            if montant_retrait <= self.__solde:
                self.__solde -= montant_retrait
                print(f"Retraint effectuer de {montant_retrait}")
            else:
                print("Erreur solde insuffisant")
    def agios(self,taux = 5):
        if self.__solde <0:
            montant_agios = abs(self.__solde) * (taux/100)
            self.__solde -= montant_agios
            print(f"Agios de {montant_agios} € appliqués. Nouveau solde : {self.__solde} €.")
        else:
            print("Aucun agios appliqué : le solde n'est pas négatif.")
    def virement(self, compte_destinataire, montant):
        if montant > 0:
            if self.__decouvert:
                if self.__solde - montant >= -500:
                    self.__solde -= montant
                    compte_destinataire.virement(montant)
                    print(f"Virement de {montant} € effectué vers le compte de {compte_destinataire.__prenom} {compte_destinataire.__nom}.")
                else:
                    print("Erreur : Limite de découvert atteinte (-500 €). Virement impossible.")
            else:
                if montant <= self.__solde:
                    self.__solde -= montant
                    compte_destinataire.versement(montant)
                    print(f"Virement de {montant} € effectué vers le compte de {compte_destinataire.__prenom} {compte_destinataire.__nom}.")
                else:
                    print("Erreur : Solde insuffisant pour effectuer ce virement.")
        else:
            print("Erreur : Le montant du virement doit être positif.")

compte = CompteBancaire("52613","Dave","Batista",13000,True)
print(compte.afficher())
compte.afficherSolde()
compte.set_versement(200)
compte.retrait(300)
compte.afficherSolde()

compte2 = CompteBancaire("44267","Cena","John",-400,True)
print(compte2.afficher())

montant_virement = abs(compte2.get_solde())
compte.virement(compte2, montant_virement)