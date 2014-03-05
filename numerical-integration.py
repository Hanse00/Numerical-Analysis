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
segment_size = 0.0
current_x = 0.0
total_sum = 0.0
percent_cycle = 0


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

    #Calculate number of cycles to take up one percent of the total calculation
    percent_cycle = number_of_segments / 100

    #Calculate segment size value span / number of segments
    segment_size = (x_max - x_min) / number_of_segments

    #For every segment
    for i in range(number_of_segments):
        #If one percent is more than a single cycle
        #And the current i value is one of a pull percentage
        #Print how for along program is
        if percent_cycle >= 1 and i % percent_cycle == 0:
            print str((i / percent_cycle) + 1) + "%"
            
        #Caulcuate the x value for the current segment
        current_x = x_min + (segment_size * i)
        
        #Add the sum for the current segment to the total sum
        #X used is the middle of the current segment (x + half segment)
        total_sum = total_sum + calc(function, current_x + (0.5 * segment_size)) * segment_size

    print total_sum
