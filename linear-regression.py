"""
Take a two dimensional list of x,y coordinates.
Return liniear expression calculated by the least squares method.
"""

import sys

#Define global values
pairs = []
sumx = 0
sumy = 0

#Number of pairs is half the number of values, excluding script name
pair_num = (len(sys.argv) - 1) / 2
print "Pairs inputted: " + str(pair_num)

for i in range(pair_num):
    #Every other value is an x value, starting from index 1
    x = (i * 2) + 1
    y = x + 1

    #Debug code
    print "(" + str(sys.argv[x]) + ", " + str(sys.argv[y]) + ")"

    #Save input as two dimensional list
    pairs.append([sys.argv[x],sys.argv[y]])

#Debug code
print pairs

#Sum x and y values
for i in pairs:
    sumx = sumx + int(i[0])
    sumy = sumy + int(i[1])

print "Sum of x values: " + str(sumx)
print "Sum of y values: " + str(sumy)
