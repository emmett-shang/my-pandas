import math
from decimal import *
getcontext().prec = 50

pi = 0
polysides = 6
sidelen = 1
perim = 6
dia = 2

while polysides < 1000000000000000000000000000000:
    sidelen2 = Decimal(sidelen) / Decimal(2)
    radius_a = Decimal(((1**2)-(sidelen/2)**2)).sqrt()
    radius_b = Decimal(1) - Decimal(radius_a)
    sidelennew = Decimal((radius_b**2)+(sidelen2**2)).sqrt()
    polycircum = Decimal(polysides * sidelen)
    pi = polycircum / dia
    print('Polygon Sides:', polysides, 'pi=', format(pi, '0.50'))
    sidelen = sidelennew
    polysides = polysides * 2