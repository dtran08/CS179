# Medical Database Visualization Tool Project Logistics

## What is this?
Our senior design is a Medical Database Visualization Tool that uses the MIMIC-III Medical Database.

## How it works
Before even using this project, the user must first have the data from the MIMIC-III Medical Database. This is attainable through https://mimic.physionet.org/gettingstarted/access/. After obtaining the data, it goes through filtering and cleaning in order for the website to properly display the graphs and information from the data. The cleaned file is then placed in the same directory as the index.html where D3 parses the csv file and has canvasJS graphs the data.

### Python Scripts
#### name_assignment.py
The file gets the PATIENT.csv and parses through, randomly assigning names using the Faker library (which you will need to install before use). The file outputs PATIENT_NAMES.csv in the same directory as the name_assignment.py file. Be sure to make sure that the location of the PATIENT.csv is correct in the code.

#### patient_care.py
The file gets the CHARTEVENTS.csv and parses through, removing chart events that don't have an item identification between 0 and 7000 (since that is carvue). The user can change the interval to change to another medical database that they prefer.

#### get_patient.py
The file gets the CHARTEVENTS.csv and gives you two options on how to parse the file: 1) splits every possible patient into their own patient file (ex. there's 100 patients in the CHARTEVENTS.csv, so there will be 100 csv files for each individual patient) and 2) enter a specific patient identification number and have it parse for only that one file. The second option was created because, depending on the size of the CHARTEVENTS.csv file, it could take up to a month (i.e. 35GB file) or longer.

## How to run
### 1. Get the data
  1. Apply for the data through https://mimic.physionet.org/gettingstarted/access//
### 2. Run Python Scripts on the CHARTEVENTS.csv file
  1. Run filter_carevue.py to only keep the data from the carevue database.
  2. Run get_patient.py. When running, it'll prompt two choices: the first choice will divide the entire database into individual patient csv files and the second choice will the prompt the user to input a specific patient.
  _NOTE_: Running the first prompt on the get_patient.py will vary in time completion depending on how big the file is.
### 3. Viewing Website
  1. Put the patient files in the same directory as the index.html in the site folder.
  2. Click on the index.html file to view the data.
