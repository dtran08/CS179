import csv
# need to install library
from faker import Faker
from faker.providers import person

# intialize faker
fake = Faker()
fake.add_provider(person)

patient_id = []
names = []

with open("data/PATIENTS.csv") as f:
    reader = csv.reader(f)
    firstLine = False

    for row in reader:
        if not firstLine:
            # set up new csv file
            with open("data/PATIENT_NAMES.csv", "w") as file:
                writer = csv.writer(file, lineterminator='\n')
                writer.writerow(['Patient ID', 'Name'])
            firstLine = True
        else:
            # makes sure only unique ID's in the file
            if row[1] not in patient_id:
                # female gender
                if row[2] == "F":
                    full_name = fake.name_female()
                    # makes sure the name is unique
                    while full_name in names:
                        full_name = fake.name_female()
                # male gender
                else:
                    full_name = fake.name_male()
                    # makes sure the name is unique
                    while full_name in names:
                        full_name = fake.name_male()
                # stores name so it can't be duplicated
                names.append(full_name)
                # sets up row to be written into document
                new_name = [row[1], full_name]
                # adds row to csv file
                with open("data/PATIENT_NAMES.csv", "a") as file:
                    writer = csv.writer(file, lineterminator='\n')
                    writer.writerow(new_name)

print("Done!")
