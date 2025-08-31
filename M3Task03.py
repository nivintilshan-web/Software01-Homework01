gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin value is low.")
    elif hemoglobin > 155:
        print("Hemoglobin value is high.")
    else:
        print("Hemoglobin value is normal.")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin value is low.")
    elif hemoglobin > 167:
        print("Hemoglobin value is high.")
    else:
        print("Hemoglobin value is normal.")
else:
    print("Invalid gender.")
