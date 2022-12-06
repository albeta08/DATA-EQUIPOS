import csv

with open('Data_equipos.csv') as f:
    reader = csv.DictReader(f)
    club_list = [i['Club'] for i in reader]
    print(club_list)
