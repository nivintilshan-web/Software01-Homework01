class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(self.current_floor)

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(self.current_floor)

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)


def main():
    b = Building(1, 10, 3)
    b.run_elevator(0, 5)
    b.run_elevator(1, 8)
    b.run_elevator(2, 3)
    b.run_elevator(0, 1)
    b.fire_alarm()

main()
