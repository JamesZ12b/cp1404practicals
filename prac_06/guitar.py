class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        this_year = 2024
        return this_year - self.year

    def is_vintage(self):
        VINTAGE_AGE=50
        return self.get_age() >= VINTAGE_AGE
