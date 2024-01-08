#Ajouter des méthodes permettant de modifier le nom du produit et son prix.
# Ainsi que
#des méthodes permettant de retourner chaque information du produit.
#Modifier le nom et le prix de chaque produit et afficher en console
# le nouveau prix des
#produits.
#La fonction print() ne doit pas être utilisée dans la classe Produit.
class Produit:
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self,prixHT,TVA):
        return prixHT + prixHT * TVA
    
    def afficher (self,prixHT,TVA):
        return "PrixTTC = ",self.CalculerPrixTTC,"PrixHT = ",prixHT,\
        "TVA = ",TVA
 
produit_1 = Produit("gants",10,19.6)

produit_2 = Produit("bonnet",12,19.6)
