import math
import sympy
from sympy import *
init_printing(use_unicode=True)

import sferics as S
import cilindrics as C
import cartesians as X

zero = symbols('zero')
#pi = symbols(u'π')
constant = symbols('C')
ux, uy, uz = symbols(u'𝑥̂,𝑦̂,𝑧̂', positive = True, integer=True)
up, uA  = symbols(u'ρ̂,ϕ̂', positive = True, integer=True)
uR, uB  = symbols(u'r̂,ϑ̂', positive = True, integer=True)

def on_x(f):
    return f.subs({
        uR : cos(S.theta)*uz + sin(S.theta)*up,
        uB : -sin(S.theta)*uz + cos(S.theta)*up
    }).subs({
        up : ux * cos(C.phi) + sin(C.phi) * uy,
        uA : -ux * sin(C.phi) + cos(C.phi) * uy,
    }).subs({
        ux : 1,
        uy : 0,
        uz : 0})

def on_y(f):
    return f.subs({
        uR : cos(S.theta)*uz + sin(S.theta)*up,
        uB : -sin(S.theta)*uz + cos(S.theta)*up
    }).subs({
        up : ux * cos(C.phi) + sin(C.phi) * uy,
        uA : -ux * sin(C.phi) + cos(C.phi) * uy,
    }).subs({
        ux : 0,
        uy : 1,
        uz : 0})

def on_z(f):
    return f.subs({
        uR : cos(S.theta)*uz + sin(S.theta)*up,
        uB : -sin(S.theta)*uz + cos(S.theta)*up
    }).subs({
        up : ux * cos(C.phi) + sin(C.phi) * uy,
        uA : -ux * sin(C.phi) + cos(C.phi) * uy,
    }).subs({
        ux : 0,
        uy : 0,
        uz : 1})


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


def sferics_to_cilindrics( Ar, Atheta, ASphi):
    '''Changes from Sferics to Cilindrics'''
    Arho = simplify(sin(S.theta) * Ar + cos(S.theta) * Atheta)
    Aphi = simplify(ASphi)
    Az = simplify( cos(S.theta) * Ar - sin(S.theta) * Atheta )
    Arho = Arho.subs({
        S.r: sqrt(C.rho**2 + C.z**2),
        S.phi: C.phi,
        S.theta: acos(C.z/(sqrt(C.rho**2 + C.z**2)))
    })
    Aphi = Aphi.subs({
        S.r: sqrt(C.rho**2 + C.z**2),
        S.phi: C.phi,
        S.theta: acos(C.z/(sqrt(C.rho**2 + C.z**2)))
    })
    Az = Az.subs({
        S.r: sqrt(C.rho**2 + C.z**2),
        S.phi: C.phi,
        S.theta: acos(C.z/(sqrt(C.rho**2 + C.z**2)))
    })
    Arho = simplify(Arho)
    Aphi = simplify(Aphi)
    Az = simplify(Az)
    return (Arho, Aphi, Az)


def functionS2C(f):
    r = f.subs(S.theta, acos(C.z/S.r)).subs({
        S.r : sqrt(C.rho**2 + C.z**2),
        S.phi : C.phi})
    return r

def functionC2X(f):
    r = f.subs(C.phi, atan( X.y / X.x )).subs({
        C.rho : sqrt(X.x**2 + X.y**2),
        C.z : X.z})
    return r

def functionS2X(f):
    c = functionS2C(f)
    x = functionC2X(c)
    return x
