import time
import csv

with open("CHARTEVENTS.csv") as f:
    #patient41 = open('41.txt', 'w')
    reader = csv.reader(f)

    patient = {}
    start = time.time()
    for row in reader:
        # if row[1] == "41" and row[2] == "101757":
            # patient41.write(" ".join(row) + "\n")
        subject_id = row[1]
        hadm_id = row[2]

        if subject_id not in patient:
            patient[subject_id] = []
            if hadm_id not in patient[subject_id]:
                patient[subject_id].append(hadm_id)
        else:
            if hadm_id not in patient[subject_id]:
                patient[subject_id].append(hadm_id)

    end = time.time()
    print("Done in " + str(end - start) + " seconds")
    search = input("Enter subject ID: ")
    while search != 'q':
        if search not in patient:
            print("Not in database! Try again.")
        else:
            print(patient[search])
        search = input("Enter subject ID: ")
