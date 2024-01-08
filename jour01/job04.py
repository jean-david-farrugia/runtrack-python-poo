class Personne:
     def __init__(self,nom,prenom):
         self.nom = nom
         self.prenom = prenom
          
     def SePresenter(self,nom,prenom):
         print("Je suis ",prenom,nom)
 
         
#Création d'une nouvelle personne
         
personne1 = Personne("Doe","John")
personne1 = Personne("Doe","John")
personne1.SePresenter("Doe","John")

personne2 = Personne("Dupond","Jean")
personne2 = Personne("Dupond","Jean")
personne2.SePresenter("Dupond","Jean")

