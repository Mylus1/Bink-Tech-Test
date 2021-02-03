import csv

with open("Python Developer Test Dataset.csv") as file:
    reader = csv.reader(file)
    next(reader)
    sorted_numbers = sorted(reader, key=lambda row: float(row[-1]))

    print(sorted_numbers[0:5])







        

    


    
   

    
        


    