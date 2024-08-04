from prac_09.unreliable_car import UnreliableCar

reliable_car = UnreliableCar("911", 100, 99)
unreliable_car = UnreliableCar("Ferrari", 100, 1)
reliable_car.drive(40)
unreliable_car.drive(40)
print(reliable_car)
print(unreliable_car)


