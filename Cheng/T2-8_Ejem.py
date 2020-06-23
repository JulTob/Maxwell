

import electrostatics
from electrostatics import *

'''
EJemplo 2-8
Suponiendo que una nube de electrones
confinada en una region entre dos esferas
con radios de 2 y 5 cm
tiene una densidad de carga de
-3 x 10^-8
__________ cos2(ϕ)  [C/m3]
  R^4

encuentre la carga total contenida en la región
'''
print("===========")

phi = S.phi
r = S.r
dens_carg = -3 * pow(10,-8) * (cos(phi) * cos(phi)) / (r*r*r*r)

carga = S.volumetric_integral(
    dens_carg,
    r0 = 0.02,
    rf = 0.05)

pprint(dens_carg)
pprint(carga)

print("===========")
