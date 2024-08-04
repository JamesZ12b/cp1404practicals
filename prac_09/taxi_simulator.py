from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

current_taxi = None
def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0.00
    MENU="q)uit, c)hoose taxi, d)rive"
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'C':
            count = print_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            while taxi_choice >=count or taxi_choice < 0:
                print("Invalid taxi choice")
                taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif choice == 'D':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive.")
            else:
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
                current_taxi.start_fare()
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    print_taxis(taxis)

def print_taxis(taxis):
    count = 0
    print("Taxis available:")
    for taxi in taxis:
        count += 1
        print(f"{count - 1} - {taxi}")
    return count


main()