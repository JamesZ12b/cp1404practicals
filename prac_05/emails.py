email = input("Email: ")
storage_list = {}
while email != "":
    name_list = email.split("@")[0].split(".")
    capital_name_list = [name.title() for name in name_list]
    name = " ".join(capital_name_list)
    confirm_name = input(f"Is your name {name}? (Y/n)").upper()
    if confirm_name != "Y" and confirm_name != "":
        name = input("Name: ")
    storage_list[name] = email
    email = input("Email: ")

print()
for name, email in storage_list.items():
    print(f"{name} ({email})")
