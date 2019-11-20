import math

import coordinates
from coordinates import *

theta = C.theta
rho = C.rho
z = C.z

'''Suponiendo  que  un  campo  vectorial
 expresado  en  coordenadas  cilíndricas
  es'''

Ar = 3 * cos(theta)
Ath = -2 * rho
Az = z
'''¿Cuál es el campo en el punto  '''
print(u" P(4,60º,5)")
''' En Cartesianas'''
(Pr, Pth, Pl) = (
    4, math.radians(60), 5
    )

Vx, Vy, Vz = cilindrics_to_cartesians(Ar, Ath, Az)

(Px,Py,Pz) = PointC2X(4, math.radians(60), 5)

Ax, Ay, Az = FieldC2X(
            Ar, Ath, Az,
            Pr, Pth, Pl)

print(N(Ax),Ay,N(Az))
print(Px,Py,Pz)
