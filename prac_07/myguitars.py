import csv
from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Main function to read,sort and display guitars."""
    """Main function to read, display, sort, and display guitars."""
    guitars = read_csv()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_csv():
    """Read the CSV file and create a list of guitar."""
    guitars = []
    with open(FILENAME, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
                name, year, cost = row
                year = int(year)
                cost = float(cost)
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    return guitars


def guitar_lt(self, other):
    return self.year < other.year


setattr(Guitar, "__lt__", guitar_lt)

if __name__ == '__main__':
    main()
