numbers = []

while True:
    value = input("Enter a number (or press Enter to quit): ")
    if value == "":
        break
    numbers.append(float(value))

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
