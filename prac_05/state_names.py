"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
MAX_NAME_LENTH = 3
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for name, full_name in CODE_TO_NAME.items():
    print(f"{name:{MAX_NAME_LENTH}} is {full_name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
