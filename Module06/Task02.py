import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter number of sides on the dice: "))
while True:
    result = roll_dice(sides)
    print(result)
    if result == sides:
        break
