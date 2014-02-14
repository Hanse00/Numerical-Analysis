import sys
from math import *

function = ""
x = 0.0

if sys.argv < 3:
    print "Too little arguments!"
    print "Usage: numerical-differentation.py <function> <x value>"
    sys.exit(-1)
else:
    function = sys.argv[1]
    x = float(sys.argv[2])
    y = eval(function)
    print y
