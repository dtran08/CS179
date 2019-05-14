# from elasticsearch import helpers, Elasticsearch
import csv
import pprint

# es = Elasticsearch()

filename = input("Enter patient file: ")
total_items = {}
repeated = {}

with open(filename + ".csv") as f:
    reader = csv.reader(f)

    firstLine = False
    for row in reader:
        item = row[4]
        if not firstLine:
            firstLine = True
        if item not in total_items:
            total_items[item] = 1
        else:
            total_items[item] += 1

    print(len(total_items))
    for key, value in total_items.items():
        if value not in repeated:
            repeated[value] = []
        repeated[value].append(key)

    #for key, value in sorted(repeated.items(), key=lambda item: item[1]):
        #print("%s: %s" % (key, value))

with open(filename + "_items.txt", 'w') as file:
    for i in sorted(repeated):
        print("%s: %s" % (i, repeated[i]), file=file)
