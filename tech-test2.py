import csv

with open("Python Developer Test Dataset.csv") as file:
    reader = csv.reader(file)
    next(reader)
    sorted_numbers = sorted(reader, key=lambda row: float(row[-1]))
    lease_years_total = []

    for row in sorted_numbers:
        lease_years = int(row[-2])
        if lease_years == 25:
            print(row)
            lease_years_total.append(float(row[-1]))

    total_rent = sum(lease_years_total)
    print(total_rent)