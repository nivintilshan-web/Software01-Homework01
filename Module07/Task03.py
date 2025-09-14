def add_airport(airports):
    icao = input("Enter ICAO code: ").upper()
    name = input("Enter airport name: ")
    airports[icao] = name
    print(f"Airport {name} with ICAO code {icao} added.")

def fetch_airport(airports):
    icao = input("Enter ICAO code to fetch: ").upper()
    if icao in airports:
        print(f"Airport name: {airports[icao]}")
    else:
        print("No airport found with that ICAO code.")

def main():
    airports = {}
    while True:
        print("\nOptions:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            add_airport(airports)
        elif choice == "2":
            fetch_airport(airports)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option, please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()


