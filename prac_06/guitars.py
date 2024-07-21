from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    cost = format(cost, ".2f")
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added")
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
count = 0
name_width = max(len(guitar.name) for guitar in guitars)
cost_width = max(len(guitar.cost) for guitar in guitars)
print()
print("... snip ...")
print()
print("These are my guitars:")
for guitar in guitars:
    count += 1
    if guitar.is_vintage():
        print(f"Guitar {count}:  {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:>{cost_width}} (vintage)")
    else:
        print(f"Guitar {count}:  {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:>{cost_width}}")
