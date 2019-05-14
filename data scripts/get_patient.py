# from elasticsearch import helpers, Elasticsearch
import time
import csv

# es = Elasticsearch()


with open("CHARTEVENTS.csv") as f:
    reader = csv.reader(f)

    patient = input("Enter subject ID: ")
    hadmn = input("Enter hadmn ID: ")


    firstLine = False
    with open(patient + '.csv', 'w') as patient_doc:
        writer = csv.writer(patient_doc, lineterminator='\n')
        for row in reader:
            if not firstLine:
                #for val in row:
                writer.writerow(row)
                firstLine = True
            if row[1] == str(patient) and row[2] == str(hadmn):
                #for val in row:
                writer.writerow(row)
