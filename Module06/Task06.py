import math

def unit_price(diameter, price):
    radius = diameter / 2 / 100
    area = math.pi * radius * radius
    return price / area

d1 = float(input("Enter diameter of first pizza (cm): "))
p1 = float(input("Enter price of first pizza (€): "))
d2 = float(input("Enter diameter of second pizza (cm): "))
p2 = float(input("Enter price of second pizza (€): "))

u1 = unit_price(d1, p1)
u2 = unit_price(d2, p2)

if u1 < u2:
    print("First pizza is better value")
else:
    print("Second pizza is better value")

