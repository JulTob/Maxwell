
#  Prerequisites

# virtualenv -p python3 maxwell
# . maxwell/bin/activate
#    pip3 install sympy

#  Runner
#  python3 test.py

import electrostatics
from electrostatics import *

R = S.r
a = S.theta
b = S.phi


V = E * R * cos(a)
'''
Ex, Ey, Ez = Electric_Field_From_Voltage_X(V)
'''
pprint(V)

pprint( functionS2C(V) )

pprint( functionS2X(V))

pprint(
    Electric_Field_From_Voltage_X(
        functionS2X(V)
    ) )
