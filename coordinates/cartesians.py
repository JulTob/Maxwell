#  Prereqquisites
#    pip3 install sympy
#  Runner
#  python3 vectores.py
import math
import sympy
from sympy import *

x,y,z = symbols('x,y,z')



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

P1 = (1,3,2)

print((distance_pt_line( 1, 3, 2, 3, -2, 4, 0,0,0)))
