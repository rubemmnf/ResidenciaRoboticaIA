from spatialmath import *
from math import pi

r = SO2 (-pi/2)
#print(r)

r2 = SO2 (90, unit='deg')
#print(r2)

a = [1, 0]
a_1 = r * a
#print (a_1)

a_2 = r2 * a
#print(a_2)

h1 = SE2 (pi/2)
#print (h1)

h2 = SE2 (1,2)
#print(h2)

h3 = h1 * h2
#print(h3)

a_1 = h1 * a
a_2 = h2 * a
a_3 = h3 * a

print(a_1)
print(a_2)
print(a_3)