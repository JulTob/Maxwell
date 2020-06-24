

import electrostatics
from electrostatics import *



'''
Exercicio 2.9
Determinar el campo electrico
'''
print("=====================")
r = S.r; th = S.theta;
E = Electric_Field

V = E * r * cos(th)
pprint(V)

E1 = Electric_Field_From_Voltage_S(V)
pprint(E1)


print("=====================")
