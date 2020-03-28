
# calculate the area and circumference of circle. Ak user for the radius.

import math
radius = input('Enter circle radius:')

radius = float(radius)
area = math.pi * math.pow(radius, 2)

circumference = 2 * math.pi * radius

# https: // www.mathsisfun.com/geometry/circle-area.html
print('The area of circle for radius',  radius, ' is :', round(area, 2))
print('The circumference of circle for radius',
      radius, ' is :', round(circumference, 2))
