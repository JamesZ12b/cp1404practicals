import random

random_numbers=[]
picks=int(input("How many quick picks: "))



for i in range(6):
    random_numbers[i] = random.randint(1, 45)
    random_numbers.append(random_numbers[i])
    random_numbers.sort()


set_numbers = set(random_numbers)
for num in random_numbers:
    if num in set_numbers:
        print(num,end=" ")
    else:
        number = random.randint(1, 45)
        random_numbers.append(number)
        print(num,end=" ")






