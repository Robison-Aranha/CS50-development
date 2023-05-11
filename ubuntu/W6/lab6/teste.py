import csv
import sys

teams = []

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for i in reader:
        teams.append(i)

print(teams)