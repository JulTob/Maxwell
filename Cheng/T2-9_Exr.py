

import electrostatics
from electrostatics import *

'''
Exercicio 2.9
Formula de la superficie de una esfera
'''
print("===========")
r = S.r

supf = diff(
    S.volumetric_integral(
    1,
    r0 = 0,
    rf = r),
    r)

pprint(supf)

print("===========")
