import csv


desired_wage = 40000
high_wages_norm = []
high_wages = []

# Accessing wage_information.csv normally
with open('wage_information.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        annual_wage = int(row[2])
        if annual_wage >= desired_wage:
            high_wages_norm.append(row)

print(high_wages)
with open('high_wages_norm.txt', 'w') as outfile:
    writer = csv.writer(outfile)
    for row in high_wages_norm:
        writer.writerow(row)

# Accessing wage_information.csv using csv.DictWriter and csv.DictReader


with open('wage_information.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    
    for row in reader:
        if int(row['annual_wage']) >= desired_wage:
            high_wages.append(row)

print(high_wages)
with open('high_wages.txt', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=high_wages[0].keys())
    writer.writeheader()
    for row in high_wages:
        writer.writerow(row)