import os
import csv
from collections import Counter

csvpath = os.path.join('Resources', 'election_data.csv')

candidates = []
votes_per = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvfile)

    for row in csvreader:

        candidates.append(row[2])
        
    count = Counter(candidates)
    votes_per.append(count.most_common())
    
    for x in votes_per:
        first = format((x[0][1])*100/(sum(count.values())),'.3f')
        second = format((x[1][1])*100/(sum(count.values())),'.3f')
        third = format((x[2][1])*100/(sum(count.values())),'.3f')
        fourth = format((x[3][1])*100/(sum(count.values())),'.3f')

    
print("Results")
print("----------------------------")
print(f"Total Votes:  {sum(count.values())}")
print("----------------------------")
print(f"{votes_per[0][0][0]}: {first}% ({votes_per[0][0][1]})")
print(f"{votes_per[0][1][0]}: {second}% ({votes_per[0][1][1]})")
print(f"{votes_per[0][2][0]}: {third}% ({votes_per[0][2][1]})")
print(f"{votes_per[0][3][0]}: {fourth}% ({votes_per[0][3][1]})")
print("----------------------------")
print(f"Winner:  {votes_per[0][0][0]}")
print("----------------------------")

results = os.path.join("results", "election_data.txt")
with open(results, "w") as outfile:

    outfile.write("Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes_per[0][0][0]}: {first}% ({votes_per[0][0][1]})\n")
    outfile.write(f"{votes_per[0][1][0]}: {second}% ({votes_per[0][1][1]})\n")
    outfile.write(f"{votes_per[0][2][0]}: {third}% ({votes_per[0][2][1]})\n")
    outfile.write(f"{votes_per[0][3][0]}: {fourth}% ({votes_per[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votes_per[0][0][0]}\n")
    outfile.write("-------------------------\n")