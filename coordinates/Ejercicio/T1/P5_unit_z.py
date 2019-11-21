
#  Prerequisites

# virtualenv -p python3 maxwell
# . maxwell/bin/activate
#    pip3 install sympy

#  Runner
#  python3 test.py

import math

import coordinates
from coordinates import *
pi = symbols(u'π')

z = C.z

'''
Exprese el vector unitario zuˆ
en coordenadas esféricas
'''
Arho = C.rho
ACtheta = C.theta
Al = z
(Ar, Aphi, Atheta) = cilindrics_to_sferics(
    Arho.subs({C.rho:0}),
    ACtheta.subs({C.theta:0}),
    Al.subs({z:1})
    )
print(
    Ar.subs(C.rho,0).subs(C.theta,0), " , ",
    Aphi.subs(C.rho,0).subs(C.theta,0), " , ",
    Atheta.subs(C.rho,0).subs(C.theta,0))

