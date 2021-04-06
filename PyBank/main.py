import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = list(csv.reader(csvfile, delimiter= ","))
    
    months = len(csvreader) - 1
    
    
    print(months)
    

    
