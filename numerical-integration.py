"""
Takes a function, min value, max value and number of segments.
Return gradient in point x.
"""

import sys
from math import *

#Calculate inserted function for value x
def calc(function, x):
    return eval(function)

#Define input variables
function = ""
x_min = 0.0
x_max = 0.0
number_of_segments = 0

#Define helper variables



#Exit if an insufficient number of variables have has been entered 
if len(sys.argv) < 5:
    print "Too little arguments!"
    print "Usage: numerical-differentation.py <function> <min value> <max value> <number of segements>"
    sys.exit(-1)
else:
    #Assign variables from arguments
    function = sys.argv[1]
    x_min = float(sys.argv[2])
    x_max = float(sys.argv[3])
    number_of_segments = int(sys.argv[4])
