# Made by belain3d. Git Repo on https://github.com/belain3d/Fun-Projects #

def gyok(a, b):
    return a**b

# ---------------------------------------------- Síkidomok ---------------------------------------------- #

class teglalap:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def Terulet(self):
        return self.a*self.b

    def Kerulet(self):
        return 2*(self.a+self.b)

class negyzet:
    def __init__(self, a):
        self.a = a
    
    def Terulet(self):
        return self.a*self.a

    def Kerulet(self):
        return 4*self.a

    def Atlo(self):
        return gyok(self.a**2+self.a**2)

class haromszog:
    def __init__(self, a=0, b=0, c=0, m=0):
        self.a = a
        self.b = b
        self.c = c
        self.m = m

    def Terulet(self):
        return (self.a*self.m)/2
    
    def Kerulet(self):
        return self.a+self.b+self.c

class derekszoguharomszog:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    
    def Terulet(self):
        return (self.a*self.b)/2

    def Kerulet(self):
        return self.a+self.b+self.c

class kor:
    def __init__(self, r=0, d=0):
        self.r = r
        self.d = d

    def Terulet(self):
        return 3.14*self.r**2

    def Kerulet(self):
        return 2*3.14*self.r

    def Atmero(self):
        return 2*self.r

# ---------------------------------------------- Testek ---------------------------------------------- #

class teglatest:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def Terfogat(self):
        return self.a*self.b*self.c

    def Felszin(self):
        return 2*((self.a*self.b)+(self.a*self.c)+(self.b*self.c))

    def Testatlo(self):
        return gyok((self.a**2)+(self.b**2)+(self.c**2), 0.5)