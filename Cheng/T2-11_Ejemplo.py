

import electrostatics
from electrostatics import *



'''
Ejemplo 2.11
La densidad de flujo magnetico 𝔹 alrededor
de un alambre muy largo que transporta
una corriente es circunferencial
e inversamente proporcional a
la distancia del alambre.

Calcule 𝛁·𝔹

'''
print("=====================")
'''Situamos el alambre en el eje z'''
rho,phi,z = C.rho, C.phi, C.z

cons = symbols('k')
# Constant

B = uA * cons / rho
pprint(B)

Div = C.divergence(
    on_rho(B),
    on_phi(B),
    on_z(B))
pprint(Div)
'''
 𝛁·𝔹 = 0
 Campo solenoidal
 '''

print("=====================")
