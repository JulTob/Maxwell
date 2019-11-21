#  Prereqquisites
#    pip3 install sympy
#  Runner
#  python3 vectores.py
import math
import sympy
from sympy import *

x,y,z = symbols(u'𝑥,𝑦,𝑧')



def modulus( Ax, Ay, Az):
    "Module of a vector"
    result = math.sqrt(Ax*Ax+Ay*Ay+Az*Az);
    return result;

def unitarium( Ax, Ay, Az):
    "Unitarium of a vector"
    r = modulus( Ax, Ay, Az)
    return Ax/r, Ay/r, Az/r;

def dot_product(Ax, Ay, Az, Bx, By, Bz):
    "Dot Product of two vectors"
    result = Ax * Bx + Ay * By + Az * Bz
    return result


def angle_radians(Ax, Ay, Az, Bx, By, Bz):
    "Change of basis to cilindricals"
    cos_angle = dot_product(Ax, Ay, Az, Bx, By, Bz) / (modulus( Ax, Ay, Az) * modulus( Bx, By, Bz))
    angle = math.acos(cos_angle)
    return angle;

def angle(Ax, Ay, Az, Bx, By, Bz):
    "Change of basis to cilindricals"
    cos_angle = dot_product(Ax, Ay, Az, Bx, By, Bz) / (modulus( Ax, Ay, Az) * modulus( Bx, By, Bz))
    angle = math.degrees(math.acos(cos_angle))
    return angle;


def cross_product(Ax, Ay, Az, Bx, By, Bz):
    "Cross Product of two vectors"
    Rx = Ay * Bz - Az * By
    Ry = Az * Bx - Ax * Bz
    Rz = Ax * By - Ay * Bx
    return Rx, Ry, Rz

def difference(Ax, Ay, Az, Bx, By, Bz):
    "Cross Product of two vectors"
    Rx = Bx - Ax
    Ry = By - Ay
    Rz = Bz - Az
    return Rx, Ry, Rz

def distance_pt_line(D_L_x, D_L_y, D_L_z,L0_x, L0_y, L0_z, Px, Py, Pz):
    "Distance Point to line through a line-point"
    # recta = D_L · l + L0
    u_mod = modulus(D_L_x,D_L_y,D_L_z)
    topx, topy, topz = cross_product( Px-L0_x, Py-L0_y, Pz-L0_z, D_L_x,D_L_y,D_L_z)
    top = modulus(topx, topy, topz )
    return top/u_mod

def evaluate(Ax, Ay, Az, Px,Py,Pz):
    "Evaluate at point"
    Rx = simplify(Ax.subs(x,Px).subs(y,Py).subs(z,Pz))
    Ry = simplify(Ay.subs(x,Px).subs(y,Py).subs(z,Pz))
    Rz = simplify(Az.subs(x,Px).subs(y,Py).subs(z,Pz))

    return (Rx, Ry, Rz)


def volumetric_integral(
    f,
    x0 = 0,
    xf = x,
    y0 = 0,
    yf = y,
    z0 = 0,
    zf = z):
    ''' Integrates in cilindrics'''
    result = f
    result = integrate(result,(x, x0, xf))
    result = integrate(result,(y, y0, yf))
    result = integrate(result,(z, z0, zf))
    return result

def gradient(U):
    Vx = diff(U,x)
    Vy = diff(U,y)
    Vz = diff(U,z)
    return (Vx, Vy, Vz)
