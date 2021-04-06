import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
monthlychanges = []

month_count = 0
net_profit = 0
prev_profit = 0
current_profit = 0
profit_change = 0

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)

    for row in csvreader:
        month_count +=  1
        current_profit = int(row[1])
        net_profit += current_profit

        if (month_count == 1):
            prev_profit = current_profit
            
            continue
        
        else:
            profit_change = current_profit - prev_profit

            months.append(row[0])
            monthlychanges.append(profit_change)
            
            prev_profit = current_profit

avg_profit = round(net_profit/(month_count - 1), 2)

max_change = max(monthlychanges)
min_change = min(monthlychanges)

max_month_index = monthlychanges.index(max_change)
min_month_index = monthlychanges.index(min_change)

max_month = months[max_month_index]
min_month = months[min_month_index]

print('Analysis')
print('-----------------------')
print(f"Total number of months: {month_count}")
print(f"Total: ${net_profit}")
print(f"Average change: ${avg_profit}")
print(f"Greatest increase: {max_month} ${max_change}")
print(f"Greatest decrease: {min_month} ${min_change}")

analysis = os.path.join('Analysis', 'analysis.txt')
with open(analysis, 'w') as textfile:
    textfile.write('Analysis\n')
    textfile.write('-----------------------\n')
    textfile.write(f"Total number of months: {month_count}\n")
    textfile.write(f"Total: ${net_profit}\n")
    textfile.write(f"Average change: ${avg_profit}\n")
    textfile.write(f"Greatest increase: {max_month} ${max_change}\n")
    textfile.write(f"Greatest decrease: {min_month} ${min_change}\n")