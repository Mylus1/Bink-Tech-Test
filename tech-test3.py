import csv

with open("Python Developer Test Dataset.csv") as file:
    reader = csv.reader(file)
    next(reader)
    sorted_numbers = sorted(reader, key=lambda row: float(row[-1]))


tenant_and_masts={
    
}

for row in sorted_numbers:
    if row[-5] in tenant_and_masts:
        tenant_and_masts[row[-5]] += 1
    else:
        tenant_and_masts[row[-5]] = 1
for d in tenant_and_masts:
    print(d, tenant_and_masts[d])
