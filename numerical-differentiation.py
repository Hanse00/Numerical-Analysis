"""
Take a function, x value to calculate coefficient for, and h spread value.
Return gradient in point x.
"""

import sys
from math import *

#Calculate inserted function for value x
def calc(function, x):
    return eval(function)

#Define global variables
function = ""
x = 0.0
h = 0.0
gradient = 0.0

#Exit if an insufficient number of variables have has been entered 
if len(sys.argv) < 4:
    print "Too little arguments!"
    print "Usage: numerical-differentation.py <function> <x value> <h value>"
    sys.exit(-1)
else:
    #Assign variables from arguments
    function = sys.argv[1]
    x = float(sys.argv[2])
    h = float(sys.argv[3])

    #Calculate gradient by function:
    #gradient = (f(x + h) - f(x - h)) / (2 * h)
    gradient = (calc(function, x + h) - calc(function, x - h)) / (2 * h)

    print "%.4f" % gradient
