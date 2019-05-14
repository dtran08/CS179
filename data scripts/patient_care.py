# from elasticsearch import helpers, Elasticsearch
import csv
import pprint

patients = {}

# es = Elasticsearch()
with open("CHARTEVENTS.csv") as f:
    #patient41 = open('41.txt', 'w')
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        item = int(row[4])
        patient = row[1]

        if patient not in patients:
            patients[patient] = []
        if item <= 70000 and item > 0:
            if "carvue" not in patients[patient]:
                patients[patient].append("carevue")
        elif item >= 70001 and item <= 220003:
            if "hospital" not in patients[patient]:
                patients[patient].append("hospital")
        else:
            if "metavision" not in patients[patient]:
                patients[patient].append("metavision")

with open("patient_care.txt", 'w') as file:
    for i in sorted(patients):
        print("%s: %s" % (i, patients[i]), file=file)
