while True:
    inches = float(input("Enter length in inches: "))
    if inches < 0:
        break
    print(inches * 2.54, "cm")
