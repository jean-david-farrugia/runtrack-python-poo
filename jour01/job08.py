import math
class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon

    def changerRayon(self,rayon):
        self.rayon = rayon
    
    def afficherInfos(self,rayon):
        print(f"Le cercle a pour rayon {self.rayon} cm")
    
    def circonference(self,rayon):
        return print("Circonference du cercle = ",2 * math.pi * rayon)
    
    def aire(self,rayon):
        return print("Aire du cercle = ",math.pi * rayon**2)

    def diametre(self,rayon):
        return print("Diametre = ",2 * rayon)

cercle_1 = Cercle(4)

cercle_1.afficherInfos(4)
cercle_1.aire(4)
cercle_1.circonference(4)
cercle_1.diametre(4)

cercle_2 = Cercle(7)

cercle_2.afficherInfos(7)
cercle_2.aire(7)
cercle_2.circonference(7)
cercle_2.diametre(7)
