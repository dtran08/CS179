# from elasticsearch import helpers, Elasticsearch
import time
import csv

# es = Elasticsearch()


#with open("CHARTEVENTS.csv") as f:
    #reader = csv.reader(f)

    #patient = input("Enter subject ID: ")
    #hadmn = input("Enter hadmn ID: ")


    #firstLine = False
    #with open(patient + '.csv', 'w') as patient_doc:
        #writer = csv.writer(patient_doc, lineterminator='\n')
        #for row in reader:
            #if not firstLine:
                #for val in row:
                #writer.writerow(row)
                #firstLine = True
            #if row[1] == str(patient):
                #if row[4] <= 70000:
                    #for val in row:
                    #writer.writerow(row)

existing = []

with open("CLEANED_CHARTEVENTS.csv") as f:
    reader = csv.reader(f)

    firstLine = False
    for row in reader:
        patient_id = row[1]
        if not firstLine:
            header = row
            firstLine = True
        if patient_id not in existing:
            with open(patient_id + ".csv", "w") as new_doc:
                writer = csv.writer(new_doc, lineterminator='\n')
                writer.writerow(header)
                writer.writerow(row)
            existing.append(patient_id)
        else:
            with open(patient_id + ".csv", "a") as curr_doc:
                writer = csv.writer(curr_doc, lineterminator='\n')
                writer.writerow(row)
