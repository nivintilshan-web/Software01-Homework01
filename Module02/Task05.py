talents = int(input("Enter the number of talents (leiviskä): "))
pounds = int(input("Enter the number of pounds (naula): "))
lots = int(input("Enter the number of lots (luoti): "))

total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("Equivalent mass:")
print(kilograms, "kilograms and", round(grams, 2), "grams")