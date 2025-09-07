def gallons_to_liters(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input("Enter volume in gallons (negative to quit): "))
    if gallons < 0:
        break
    liters = gallons_to_liters(gallons)
    print(liters)
