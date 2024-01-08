class Point:
     def __init__(self,x,y):
         self.x = x
         self.y = y
     def afficherLesPoints(self,x,y):
         print("Les coordonnées des points sont : ",x,"et",y)
     def afficherX(self,x):
         print("x est égal à :",x)
     def afficherY(self,y):
         print("y est égal à :",y)
     def changerX(self,x):
         self.x = x
     def changerY(self,y):
         self.y = y
