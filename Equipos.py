import csv

with open('Data_equipos.csv') as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i['Club'])

#Club,Competition,