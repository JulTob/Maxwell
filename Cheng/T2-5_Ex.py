
#  Prerequisites

# virtualenv -p python3 maxwell
# . maxwell/bin/activate
#    pip3 install sympy

#  Runner
#  python3 test.py

import electrostatics
from electrostatics import *

P1 =  1 * ux + 3 * uy + 2 * uz
P2 =  3 * ux + -2 * uy + uz * 4


print("===========")
pprint(P1)
pprint(P2)

a = P2-P1
print("a) ")
pprint(a)

b = X.modulus(
    on_x(a), on_y(a), on_z(a) )
print("b) ")
pprint(b)

c = X.distance_pt_line(
    on_x(P2), on_y(P2), on_z(P2),
    on_x(P1), on_y(P1), on_z(P1),
    0, 0, 0
    )
print("c) ")
pprint(c)

print("===========")
