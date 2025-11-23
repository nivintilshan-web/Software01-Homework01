class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def main():
    car = Car("ABC-123", 142)
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print(car.current_speed)
    car.accelerate(-200)
    print(car.current_speed)
    car.current_speed = 60
    car.travelled_distance = 2000
    car.drive(1.5)
    print(car.travelled_distance)

main()
