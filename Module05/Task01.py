import random

n = int(input("How many dice to roll? "))
total = 0
for i in range(n):
    total += random.randint(1, 6)
print("Sum:", total)
