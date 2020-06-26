

import electrostatics
from electrostatics import *



'''
Exercicio 2.9
Determinar el campo electrico
'''
print("=====================")
x = X.x
y = X.y
z = X.z

Div = X.divergence(x,y,z)
pprint(Div)


rho,phi,z = C.rho, C.phi, C.z
Div = C.divergence(rho,0,z)
pprint(Div)


r,theta,fi = S.r, S.theta, S.phi
Div = S.divergence(r,0,0)
pprint(Div)

print("=====================")
