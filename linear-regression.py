"""
Take a two dimensional list of x,y coordinates.
Return liniear expression calculated by the least squares method.
"""

import sys

#Define global values
pairs = []
sum_x = 0.0
sum_y = 0.0
sum_xy = 0.0
sum_x_squared = 0.0
avenrage_x = 0.0
avenrage_y = 0.0
gradient = 0.0
y_intercept = 0.0

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
    pairs.append([float(sys.argv[x]),float(sys.argv[y])])

#Debug code
print pairs

#Sum x and y values
for i in pairs:
    sum_x = sum_x + i[0]
    sum_y = sum_y + i[1]

average_x = sum_x / pair_num
average_y = sum_y / pair_num

#Debug code
print "Sum of x values: " + str(sum_x)
print "Sum of y values: " + str(sum_y)

print "Average of x values: " + str(average_x)
print "Average of y values: " + str(average_y)
#Debug end

#Sum of x * y is x * y for each pair added together
for i in pairs:
    sum_xy = sum_xy + (i[0] * i[1])

#Debug code
print "Sum of x * y is: " + str(sum_xy)

for i in pairs:
    sum_x_squared = sum_x_squared + (i[0] ** 2)

#Debug code
print "Sum of x squared is: " + str(sum_x_squared)

gradient = (sum_xy - pair_num * average_x * average_y) / (sum_x_squared - pair_num * average_x ** 2)

#Debug code
print "Gradient is: " + str(gradient)

y_intercept = average_y - (gradient * average_x)

#Debug code
print "Y intercept is: " + str(y_intercept)

print "Formula : y = %.4fx + %.4f" % (gradient, y_intercept)
