import math
import sympy
from sympy import *

r, theta, phi = symbols(u'r, ϑ, ϕ')
#pi = symbols(u'π')
'''
r : Real
ϑ : 0..π   theta
ϕ : 0..2π  phi
'''

def modulus( A_r, A_phi, A_theta):
    "Module of a vector"
    return A_r;

def unitarium( A_r, A_phi,A_theta):
    "Unitarium of a vector"
    return 1, A_phi, A_theta;

def volumetric_integral(
    f,
    r0 = 0,
    rf = r,
    phi0 = 0,
    phif = 2*pi,
    theta0 = 0,
    thetaf = pi):
    ''' Integrates in sferics'''
    result = f*r*r*sin(theta)
    result = integrate(result,(r, r0, rf))
    result = integrate(result,(phi, phi0, phif))
    result = integrate(result,(theta, theta0, thetaf))
    return result
