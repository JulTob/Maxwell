import math

def modulus( Ax, Ay, Az):
    "Module of a vector"
    result = math.sqrt(Ax*Ax+Ay*Ay+Az*Az);
    return result;

def unitarium( Ax, Ay, Az):
    "Unitarium of a vector"
    r = modulus( Ax, Ay, Az)
    return Ax/r, Ay/r, Az/r;
