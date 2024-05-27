FIRST_DISCOUNT=0.1
SECOND_DISCOUNT=0.15
sales = float(input("Enter sales: $"))
while sales>=0:
    if sales<1000:
        bonus=sales*FIRST_DISCOUNT
    else:
        bonus=sales*SECOND_DISCOUNT
    print(bonus)
    sales = float(input("Enter sales: $"))