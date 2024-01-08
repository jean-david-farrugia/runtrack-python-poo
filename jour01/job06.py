class Animal:
    def __init__(self,age,prenom):
        self.age = 0
        self.prenom = ""
    def vieillir(self,age):
        self.age = age + 1
    def nommer(self,prenom):
        self.prenom = prenom

animal1 = Animal(0,"")

print(f"L'age de l'animal {animal1.age}")
#Age de l'animal après appel de la méthode vieillir
animal1.vieillir(0)
print(f"L'age de l'animal {animal1.age}")

animal1.nommer("Luna")
print(f"L'animal se nomme {animal1.prenom}")



