length = float(input("Enter the length of the zander (in cm): "))
if length < 42:
    print("The zander is", 42 - length, "cm below the size limit. Please release it back into the lake.")
else:
    print("The zander meets the size limit. You may keep it.")
