import csv

rows = []

with open('finds.csv') as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        rows.append(row)

attributes_count = len(rows[0]) - 1
Hypothesis = rows[0]

for row in rows:
    print(row)
    for attribute in range(attributes_count):
        if row[attributes_count] == "yes":
            if row[attribute] != Hypothesis[attribute]:
                Hypothesis[attribute] = "?"

print(f"Final Hypothesis is {Hypothesis}.")
