
# calculate the area and circumference of circle. Ak user for the radius.

import math
radius = input('Enter circle radius:')

radius = int(radius)
area = math.pi * math.pow(radius, 2)

circumference = 2 * math.pi * radius


print('The area of circle for radius',  radius, ' is :', area)
print('The circumference of circle for radius',  radius, ' is :', circumference)
