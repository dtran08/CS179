import time
import csv
import datetime

start = datetime.datetime.now()

with open("CHARTEVENTS.csv") as f:
    #patient41 = open('41.txt', 'w')
    reader = csv.reader(f)
    row_number = 1

    firstLine = False
    for row in reader:
        if not firstLine:
            header = row
            with open("CLEANED_CHARTEVENTS.csv", "w") as file:
                writer = csv.writer(file, lineterminator='\n')
                writer.writerow(header)
            firstLine = True
        else:
            item = int(row[4])

            if item <= 70000 and item > 0:
                with open("CLEANED_CHARTEVENTS.csv", "a") as file:
                    writer = csv.writer(file, lineterminator='\n')
                    writer.writerow(row)
        print("row: " + str(row_number))
        row_number += 1

print("started at " + str(start))
print("finished at " + str(datetime.datetime.now()))
