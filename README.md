# Medical Database Visualization Tool Project Logistics

## What is this?
Our senior design is a Medical Database Visualization Tool that uses the MIMIC-III Medical Database.

## How it works
Before even using this project, the user must first have the data from the MIMIC-III Medical Database. This is attainable through https://mimic.physionet.org/gettingstarted/access/. After obtaining the data, it goes through filtering and cleaning in order for the website to properly display the graphs and information from the data. The cleaned file is then placed in the same directory as the index.html where D3 parses the csv file and has canvasJS graphs the data.

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
