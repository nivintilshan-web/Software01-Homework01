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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print("REG\tMAX\tSPEED\tDISTANCE")
        for car in self.cars:
            print(f"{car.registration_number}\t{car.maximum_speed}\t{car.current_speed}\t{int(car.travelled_distance)}")
        print()

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


def main():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg = f"ABC-{i}"
        cars.append(Car(reg, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            print(f"Status after {hours} hours:")
            race.print_status()

    print(f"Final status after {hours} hours:")
    race.print_status()


main()
