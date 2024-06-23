CODE_OF_COLOR = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                 "alizarin crimson": "#e32636",
                 "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7",
                 "antiquewhite1": "#faebd7", "antiquewhite2": "#eedfcc"}

color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        print(CODE_OF_COLOR[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()
