#Question 05
import math

x_1= float(input("Enter circle1's center x coordinate: "))
y_1= float(input("Enter circle1's center y-coordinates: "))
r_1= float(input("Enter circle1's radius: "))

x_2= float(input("Enter circle2's center x coordinate: "))
y_2= float(input("Enter circle2's center y-coordinates: "))
r_2= float(input("Enter circle2's radius: "))

distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)


if distance + r_2 <= r_1:
    print("circle2 is inside circle1")
elif distance <= r_1 + r_2:
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap with circle1")
