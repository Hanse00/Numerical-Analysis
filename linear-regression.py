"""
Take a two dimensional list of x,y coordinates.
Return liniear expression calculated by the least squares method.
"""

import sys

#Number of pairs is half the number of values, excluding script name.
pair_num = (len(sys.argv) - 1) / 2
print "Pairs inputted: " + str(pair_num)

for i in range(pair_num):
    #Every other value is an x value, starting from index 1.
    x = (i * 2) + 1
    y = x + 1

    print "(" + str(sys.argv[x]) + ", " + str(sys.argv[y]) + ")"
