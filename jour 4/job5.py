import math
class Forme:
    def __init__(self):
        pass
    def aire():
        return 0

class Cercle (Forme):
    def __init__(self,radius):
        self.radius = radius 
    def aire(self):
        return math.pi * (self.radius **2)

rond = Cercle(6)
print(rond.aire())
rond2 = Cercle(2)
rond3 = Cercle(15.8)
print(rond2.aire())
print(rond3.aire())
