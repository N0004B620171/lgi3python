import math


class Point:
    _x: float
    _y: float

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def afficher(self):
        print(f"POINT({self._x},{self._y})")


p = Point(1, 2)
p.afficher()


class Cercle:
    _p = Point(0, 0)
    _r: float

    def __init__(self, x, y, r):
        self._p._x = x
        self._p._y = y
        self._r = r

    def geterimetre(self):
        return 2*math.pi*self._r

    def getsurface(self):
        return math.pi*math.pow(self._r, 2)

    def appartient(self, x, y):
        p1=Point(x, y)
        if math.pow(x - self._p._x, 2)+math.pow(y - self._p._y, 2) < math.pow(self._r, 2):
            return print(f"le point {p1.afficher()} appartient au cercle ")
        else:
            return print(f"le point {p1.afficher()} n'appartient pas au cercle ")

    def afficher(self):
        print(f"CERCLE({self._p._x },{self._p._y },{self._r})")
        print(f"le perimetre du cercle est de {self.geterimetre()}")
        print(f"la surface du cercle est de {self.getsurface()}")
        self.appartient(2, 55555554)


class Cylindre(Cercle):
    hauteur:float()
    def __init__(self, x, y, r,h):
        self.hauteur=h
        super().__init__(x, y, r)

    def getVolume(self):
        print(f"la surface du cylindre est de {self.getsurface() + self.geterimetre()*self.hauteur}")
cy=Cylindre(1, 2, 3, 4)
cy.getVolume()
c = Cercle(1, 2, 3)
c.afficher()
