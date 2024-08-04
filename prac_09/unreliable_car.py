import random

from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(0, 100)
        if random_number >= self.reliability:
            distance=0
        distance_drive = super().drive(distance)
        return distance_drive
