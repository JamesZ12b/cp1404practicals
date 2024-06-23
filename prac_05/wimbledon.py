import csv

FILENAME = "wimbledon.csv"


def main():
    data_list = read_csv()
    champions = get_champions(data_list)
    print("Wimbledon Champions: ")
    for champion, number in champions.items():
        print(f"{champion} {number}")
    countries=get_countries(data_list)
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

def read_csv():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        data_list = [data for data in reader]
        return data_list

def get_champions(data_list):
    champions = {}
    for data in data_list[1:]:
        champion = data[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data_list):
    countries = []
    for data in data_list[1:]:
        countrie = data[1]
        countries.append(countrie)
    countries = set(countries)
    return countries


main()
