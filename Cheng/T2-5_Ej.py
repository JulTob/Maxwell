
#  Prerequisites

# virtualenv -p python3 maxwell
# . maxwell/bin/activate
#    pip3 install sympy

#  Runner
#  python3 test.py

import electrostatics
from electrostatics import *

P1x, P1y, P1z =  1, 2, 0
P2x, P2y, P2z = -3, 4, 0


print("===========")

# Longitud of Op2 proyected to Op1
a = X.Proyection(
    P2x, P2y, P2z  ,
    P1x, P1y, P1z
    )

print("a) ")
pprint(a)

# Area of Triangle
bx, by, bz = X.cross_product(
    P2x, P2y, P2z  ,
    P1x, P1y, P1z
    )
b = X.modulus(bx,by,bz)
b = b/2

print("b) ")
pprint(b)

print("===========")
