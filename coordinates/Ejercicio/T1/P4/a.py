import math

import coordinates
from coordinates import *

theta = l.theta
rho = l.rho
z = l.z

'''Suponiendo  que  un  campo  vectorial
 expresado  en  coordenadas  cilíndricas
  es'''

Ar = 3 * cos(theta)
Ath = -2 * rho
Az = z
'''¿Cuál es el campo en el punto  '''
print(u" P(4,60º,5)")
(Ar, Ath, Az) = l.evaluate(
    Ar, Ath, Az,
    4, math.radians(60), 5
    )
