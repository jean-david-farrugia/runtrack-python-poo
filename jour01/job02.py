#Création de la classe Operation
class Operation:
     #Constructeur
     def __init__(self,nombre1,nombre2):
         self.nombre1 = nombre1
         self.nombre2 = nombre2
 
         
#Création d'une instance de la classe Operation
         
operation1 = Operation(12,3)
#Affichage des paramètres de l'objet operation1
print("Le nombre1 est: ",operation1.nombre1)

print ("Le nombre2 est:",operation1.nombre2)
