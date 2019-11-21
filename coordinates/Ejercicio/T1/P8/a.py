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


V = Volt * exp(-x) * sin(pi*y/4)

Ex, Ey, Ez = Electric_Field_From_Voltage_X(V)

pprint(
    X.evaluate(
        Ex, Ey, Ez,
        1,1,0
        ))
