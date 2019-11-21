import math
import sympy
from sympy import *
init_printing(use_unicode=True)

import sferics as S
import cilindrics as C
import cartesians as X

zero = symbols('zero')
pi = symbols(u'π')
constant = symbols('C')



def cilindrics_to_cartesians( Arho, Atheta, Al):
    '''Changes from cilindrics to cartesians'''
    Ax = cos(C.theta) * Arho - sin(C.theta) * Atheta
    Ay = sin(C.theta) * Arho + cos(C.theta) * Atheta
    Az = Al
    Ax = Ax.subs(
            C.rho,
            sqrt(X.x*X.x+X.y*X.y)
        ).subs(
            C.theta,
            atan(X.y / X.x)
        ).subs(
            C.z,
            X.z)
    Ay = Ay.subs(
            C.rho,
            sqrt(X.x*X.x+X.y*X.y)
        ).subs(
            C.theta,
            atan(X.y / X.x)
        ).subs(
            C.z,
            X.z)
    Az = Az.subs(
            C.rho,
            sqrt(X.x*X.x+X.y*X.y)
        ).subs(
            C.theta,
            atan(X.y / X.x)
        ).subs(
            C.z,
            X.z)
    Ax = simplify(Ax)
    Ay = simplify(Ay)
    Az = simplify(Az)
    return (Ax, Ay, Az)

def C2X( Arho, Atheta, Al):
    '''Alias for Cilindric To Cartesians'''
    ( Rrho, Rtheta, Rl) = cilindrics_to_cartesians( Arho, Atheta, Al)
    return ( Rrho, Rtheta, Rl)

def PointC2X( Prho, Ptheta, Pl):
    ''' Turns Point from Cilindrics to cartesians'''
    Px = Prho * cos(Ptheta)
    Py = Prho * sin(Ptheta)
    Pz = Pl
    return (Px, Py, Pz)

def FieldC2X(Ar, Ath, Az, Pr, Pth, Pl):
    '''Turns Field value from Cilindrics to cartesians'''
    Vx, Vy, Vz = cilindrics_to_cartesians(Ar, Ath, Az)
    (Px,Py,Pz) = PointC2X(Pr, Pth, Pl)
    Ax, Ay, Az = X.evaluate(Vx, Vy, Vz, Px,Py,Pz)
    return (Ax, Ay, Az)

def cilindrics_to_sferics( Arho, ACtheta, Al):
    '''Changes from cilindrics to Sferics'''
    Ar = sin(S.phi) * Arho + cos(S.phi) * Al
    Aphi = cos(S.phi) * Arho - sin(S.phi) * Al
    Atheta = ACtheta
    Ar = Ar.subs(
            C.rho,
            S.r*sin(S.phi)
        ).subs(
            C.z,
            S.r*cos(S.phi)
        ).subs(
            C.theta,
            S.theta)
    Aphi = Aphi.subs(
            C.rho,
            S.r*sin(S.phi)
        ).subs(
            C.z,
            S.r*cos(S.phi)
        ).subs(
            C.theta,
            S.theta)
    Atheta = Atheta.subs(
            C.rho,
            S.r*sin(S.phi)
        ).subs(
            C.z,
            S.r*cos(S.phi)
        ).subs(
            C.theta,
            S.theta)
    Ar = simplify(Ar)
    Aphi = simplify(Aphi)
    Atheta = simplify(Atheta)
    return (Ar, Aphi, Atheta)
