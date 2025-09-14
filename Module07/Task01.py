
seasons = ("Winter", "Spring", "Summer", "Autumn")

def get_season(month):
    if month in (12, 1, 2):
        return seasons[0]
    elif month in (3, 4, 5):
        return seasons[1]
    elif month in (6, 7, 8):
        return seasons[2]
    elif month in (9, 10, 11):
        return seasons[3]
    else:
        return "Invalid month number!"

month = int(input("Enter the number of a month (1-12): "))
season = get_season(month)
print("The season is:", season)