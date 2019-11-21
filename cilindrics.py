import math
import sympy
from sympy import *

rho,phi,z = symbols(u'ρ,ϕ,z', real = True)
#pi = symbols(u'π')
'''
ρ : Real > 0
ϕ : 0..2π
z : Real
'''

def modulus( A_rho, A_phi, A_z):
    "Module of a vector"
    result = math.sqrt(A_rho*A_rho+A_z*A_z);
    return result;


def evaluate( A_rho, A_phi, A_z,  P_rho, P_phi, P_z):
    "Evaluate at point"
    result_rho = A_rho.subs(rho,P_rho).subs(phi,P_phi).subs(z,P_z)
    result_phi = A_phi.subs(rho,P_rho).subs(phi,P_phi).subs(z,P_z)
    result_z  = A_z.subs(rho,P_rho).subs(phi,P_phi).subs(z,P_z)
    return (result_rho, result_phi, result_z)


def volumetric_integral(
    f,
    r0 = 0,
    rf = rho,
    phi0 = 0,
    phif = 2*pi,
    z0 = 0,
    zf = z):
    ''' Integrates in cilindrics'''
    result = f*rho
    result = integrate(result,(rho, r0, rf))
    result = integrate(result,(phi, phi0, phif))
    result = integrate(result,(z, z0, zf))
    return result
