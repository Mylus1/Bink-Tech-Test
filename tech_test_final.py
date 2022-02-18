import csv
from datetime import datetime

# load the csv file
with open("Python Developer Test Dataset.csv") as file:
    reader = csv.reader(file)
    next(reader)
    global_data = list(reader)

def choice():
    print(
        """
        1. List top five masts sorted by rent
        2. Print all tenants with lease_years = 25 with total rent
        3. Print tenants with a count of their masts
        4. Print data from “Lease Start Date” between 1st June 1999 and 31st August 2007
        """
    )
    
    user_choice = input("What script would you like to run? ")
    if user_choice == "1":
        task_1()
    if user_choice == "2":
        task_2()
    if user_choice == "3":
        task_3()
    if user_choice == "4":
        task_4()

# print the top five masts sorted by rent
def task_1():
    sorted_data = sorted(global_data, key=lambda row: float(row[-1]))
    top_five = sorted_data[0:5]

    for row in top_five:
        print(row)

# print all tenants with lease_years = 25 and total rent
def task_2():
    rent_totals = []
    for row in global_data:
        if int(row[-2]) == 25:
            rent_totals.append(float(row[-1]))
            print(row)
    rent_sum = sum(rent_totals)

    print(f"Total Rent: £{rent_sum}")

# print tenant names with a count of their masts
def task_3():
    tenant_and_masts = {}
    for row in global_data:
        if row[-5] in tenant_and_masts:
            tenant_and_masts[row[-5]] += 1
        else:
            tenant_and_masts[row[-5]] = 1

    for k, v in tenant_and_masts.items():
        print(f"{k:45} : {v}")

# print data from “Lease Start Date” between 1st June 1999 and 31st August 2007
def task_4():
    def parse_date(date_format):
        return datetime.strptime(date_format, '%d %b %Y')

    def format_date(datetime_object):
            return datetime_object.strftime('%d/%m/%Y')
        
    date_format = []
    start_date = datetime(1999, 6, 1)
    end_date = datetime(2007, 8, 31)
    for row in global_data:
        date_format = row[-4]
        datetime_object = parse_date(date_format)
        datetime_string = format_date(datetime_object)
        if start_date <= datetime_object <= end_date:
            row[-4] = datetime_string

            # also re-format the lease end date
            date_format = row[-3]
            datetime_object = parse_date(date_format)
            datetime_string = format_date(datetime_object)
            row[-3] = datetime_string

            print(", ".join(row))
            print("---")
            
choice()