total=0
DISCOUNT=0.9
number=int(input("Number of items:"))
while number<0:
   print("Invalid number of items!")
   number = int(input("Number of items:"))
for i in range(number):
   price=float(input("Price of item: "))
   total=total+price
if total>100:
   total=total*DISCOUNT
print(f"Total price for {number} items is ${total:.2f}")