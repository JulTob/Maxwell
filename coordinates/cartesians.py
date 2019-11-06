import math

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

