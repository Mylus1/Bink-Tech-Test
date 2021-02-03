import csv 

with open("Python Developer Test Dataset.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    


    