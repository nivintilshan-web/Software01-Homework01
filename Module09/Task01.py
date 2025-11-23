class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

def main():
    car = Car("ABC-123", 142)

    print("Registration Number:", car.registration_number)
    print("Maximum Speed:", car.maximum_speed, "km/h")
    print("Current Speed:", car.current_speed, "km/h")
    print("Travelled Distance:", car.travelled_distance, "km")

main()
