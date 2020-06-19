
#  Prerequisites

# virtualenv -p python3 maxwell
# . maxwell/bin/activate
#    pip3 install sympy

#  Runner
#  python3 test.py

import electrostatics
from electrostatics import *

A =  up * (3 * cos(C.phi) ) \
    + uA * -2 * C.rho        \
    + uz * C.z


print("===========")
pprint(A)

a = C.evaluate(
    on_rho(A), on_phi(A), on_z(A),
    4, math.radians(60), 5
    )
pprint(a)


b = FieldC2X(
    on_rho(A), on_phi(A), on_z(A),
    4, math.radians(60), 5
    )
pprint(b)



# c

px, py, pz = PointC2X(4, math.radians(60), 5)
pprint(px)
pprint(py)
pprint(pz)




print("===========")
