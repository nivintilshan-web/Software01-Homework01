import random

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
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg = f"ABC-{i}"
        cars.append(Car(reg, max_speed))

    race_finished = False

    while not race_finished:
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

            if car.travelled_distance >= 10000:
                race_finished = True

    print("REG\tMAX\tSPEED\tDISTANCE")
    for car in cars:
        print(f"{car.registration_number}\t{car.maximum_speed}\t{car.current_speed}\t{int(car.travelled_distance)}")


main()
