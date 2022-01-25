import csv
from statistics import mean

# Open the csv file
with open('DATA475_lab_rectangles_data.csv',newline='') as f:
    reader = csv.reader(f)
    # leaving the first row for column names
    next(reader)

    # Calculating the rectagle area in areas list
    areas  = []
    for row in reader:
        width,lenght = row[1],row[2]
        area = float(width)*float(lenght)
        areas.append(area)
    
    # Creating a dictionary and printing summary of different calculations    
    summary = {    
        "Total Count":len(areas),
        "Total Area":sum(areas),
        "Min Area":min(areas),
        "Max Area":max(areas),
        "Avg Area":mean(areas),
    }
    for key,value in summary.items():
        print(f"{key}: {value}")

# Saving the summary result to a csv file
with open('summary.csv','w',newline='') as f:
    csv_file = csv.writer(f)
    csv_file.writerow(summary.keys())
    csv_file.writerow(summary.values())

