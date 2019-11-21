import math
import sympy
from sympy import *
init_printing(use_unicode=True)

import math

import coordinates
from coordinates import *

Volt = symbols(u'𝖵')


def Electric_Field_From_Voltage_X( Voltage ):
    Ex, Ey, Ez = X.gradient(Voltage)
    Ex = -Ex
    Ey = -Ey
    Ez = -Ez
    return (Ex, Ey, Ez)
