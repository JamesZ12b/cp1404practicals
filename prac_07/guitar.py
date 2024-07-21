class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        THIS_YEAR = 2024
        return THIS_YEAR - self.year

    def is_vintage(self):
        VINTAGE_AGE=50
        return self.get_age() >= VINTAGE_AGE