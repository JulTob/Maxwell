import math

def modulus( A_rho, A_phi, A_z):
    "Module of a vector"
    result = math.sqrt(A_rho*A_rho+A_z*A_z);
    return result;

