
#  Prerequisites

# virtualenv -p python3 maxwell
# . maxwell/bin/activate
#    pip3 install sympy

#  Runner
#  python3 test.py

import electrostatics
from electrostatics import *

B =  2 * ux - 6 * uy + 3 * uz


print("===========")
pprint(B)

a = X.modulus(
    on_x(B), on_y(B), on_z(B) )
print("a) ")
pprint(a)

b = X.unitarium(
    on_x(B), on_y(B), on_z(B) )
print("b) ")
pprint(b)

cx = X.angle(
    on_x(B), on_y(B), on_z(B),
    1, 0, 0 )
cy = X.angle(
    on_x(B), on_y(B), on_z(B),
    0, 1, 0 )
cz = X.angle(
    on_x(B), on_y(B), on_z(B),
    0, 0, 1 )
print("c) ")
pprint(cx)
pprint(cy)
pprint(cz)


print("===========")
