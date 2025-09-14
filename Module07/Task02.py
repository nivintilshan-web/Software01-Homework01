names = set()
while True:
    name = input("Enter a name (empty string to stop): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("\nList of entered names:")
for n in names:
    print(n)