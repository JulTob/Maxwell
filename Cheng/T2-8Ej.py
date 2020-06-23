

import electrostatics
from electrostatics import *

Px = 4
Py = -6
Pz = 12


print("===========")
pprint(Px, Py, Pz)

Pr, Pa, Pb = PointX2S(
    Px, Py, Pz)

pprint(Pr);
pprint(math.degrees(Pa));
pprint(360+math.degrees(Pb) )

print("===========")
