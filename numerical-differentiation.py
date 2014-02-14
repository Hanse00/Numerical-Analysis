import sys
from math import *

def calc(function, x):
    return eval(function)

function = ""
x = 0.0
h = 0.0

if len(sys.argv) < 4:
    print "Too little arguments!"
    print "Usage: numerical-differentation.py <function> <x value> <h value>"
    sys.exit(-1)
else:
    function = sys.argv[1]
    x = float(sys.argv[2])
    h = float(sys.argv[3])

    print calc(function, x)
