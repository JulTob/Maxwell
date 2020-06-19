
#  Prerequisites

# virtualenv -p python3 maxwell
# . maxwell/bin/activate
#    pip3 install sympy

#  Runner
#  python3 test.py

import electrostatics
from electrostatics import *
x = X.x
y = X.y

A =  5 * ux - 2 * uy + uz
Bx, By, Bz =  -3, 0, 4


print("===========")
pprint(A)
pprint(Bx*ux + By*uy + Bz*uz)

a = X.dot_product(on_x(A),on_y(A),on_z(A), Bx, By, Bz)
pprint(a)

b = X.cross_product(on_x(A),on_y(A),on_z(A), Bx, By, Bz)
pprint(b)

c = X.angle(on_x(A),on_y(A),on_z(A), Bx, By, Bz)
pprint(c)

print("===========")
