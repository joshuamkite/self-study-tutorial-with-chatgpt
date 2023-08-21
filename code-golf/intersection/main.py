"""
Arguments are 8 integers:
x1 y1 w1 h1 x2 y2 w2 h2
 0  1  2  3  4  5  6  7

https://www.geeksforgeeks.org/total-area-two-overlapping-rectangles/

 For area of intersecting part, 

x_distance for intersecting rectangle = min(r1.x, r2.x) – max(l1.x, l2.x) 
y_distance for 1st rectangle = min(r1.y, r2.y) – max(l1.y, l2.y)

If the x_distance or y_distance is negative, then the two rectangles do not intersect. In that case, overlapping area is 0.

 """

import sys

for arg in sys.argv[1:]:
    coords = list(map(int, arg.split()))
    x_overlap = (
        min((coords[0]+coords[2]), (coords[4]+coords[6])) - max(coords[0], coords[4]))
    y_overlap = (min((coords[1]+coords[3]),
                     (coords[5]+coords[7]))-max(coords[1], coords[5]))
    if x_overlap > 0 and y_overlap > 0:
        print(x_overlap*y_overlap)
    else:
        print(0)
