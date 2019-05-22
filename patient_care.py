# from elasticsearch import helpers, Elasticsearch
import csv
import pprint
import datetime

patients = {}

start = datetime.datetime.now()

# es = Elasticsearch()
with open("CHARTEVENTS.csv") as f:
    #patient41 = open('41.txt', 'w')
    reader = csv.reader(f)
    next(reader)
    row_number = 1

    for row in reader:
        item = int(row[4])
        patient = row[1]

        if patient not in patients:
            patients[patient] = []
        if item <= 70000 and item > 0:
            if "carevue" not in patients[patient]:
                patients[patient].append("carevue")
        elif item >= 70001 and item <= 220003:
            if "hospital" not in patients[patient]:
                patients[patient].append("hospital")
        else:
            if "metavision" not in patients[patient]:
                patients[patient].append("metavision")
        print("row: " + str(row_number))
        row_number += 1

with open("patient_care.txt", 'w') as file:
    for i in sorted(patients):
        print("%s: %s" % (i, patients[i]), file=file)

print("started at " + str(start))
print("finished at " + str(datetime.datetime.now()))
