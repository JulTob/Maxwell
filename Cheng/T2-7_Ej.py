

import electrostatics
from electrostatics import *

P1 = 4* up + math.radians(60) * uA + uz * 1
P2 = 3* up + math.radians(180) * uA + uz * -1


print("===========")
pprint(P1)
pprint(P2)

dr, da, dz = C.difference(
    on_rho(P1), on_phi(P1), on_z(P1),
    on_rho(P2), on_phi(P2), on_z(P2)
)
a = C.modulus(
    dr, da, dz)

pprint(a)

pprint(math.sqrt(41)) #?

print("===========")
