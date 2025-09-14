def collect_names():
    names = set()
    while True:
        name = input("Enter a name (or press Enter to stop): ").strip()
        if name == "":
            break
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)
    return names

def print_names(names):
    print("\nList of entered names:")
    for name in names:
        print(name)

def main():
    names = collect_names()
    print_names(names)

if __name__ == "__main__":
    main()
