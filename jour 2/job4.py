class Student:
    def __init__(self,nom,prenom,num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_numero_etudiant(self):
        return self.__num_etudiant
    
    def add_credits(self,credits):
        if isinstance(credits,int) and credits >0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("le nombre de credits doit etre superieur a zéro")
    def get_credits(self):
        return self.__credits
    def __student_eval(self):
        if self.__credits >= 90:
            return("excellent")
        elif self.__credits >=80:
            return("très bien")
        elif self.__credits >= 70:
            return("bien")
        elif self.__credits >= 60:
            return("passable")
        else:
            return("insuffisant")
  
    
    def student_info(self):
        print(f"Nom= {self.__nom}")
        print(f"Prenom= {self.__prenom}")
        print(f"Id= {self.__num_etudiant}")
        print(f"Niveau= {self.__level}")

eleve = Student("doe","john",145,)
eleve.add_credits(30)
print(f"le nombre de credit de {eleve.get_prenom()} {eleve.get_nom()} est de: {eleve.get_credits()}")
eleve.add_credits(40)
print(eleve.student_info())