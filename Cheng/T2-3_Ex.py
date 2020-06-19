
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

R =  - ux + 2 * uy - uz * 2


print("===========")
pprint(R)
a = X.modulus(on_x(R),on_y(R),on_z(R))

pprint(a)

b = X.unitarium(on_x(R),on_y(R),on_z(R))

pprint(b)

c = X.angle(on_x(R),on_y(R),on_z(R),0,0,1)

pprint(c)

print("===========")
