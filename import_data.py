
import csv

FILE_NAME = [
    "interactions_ai_conversions.csv",
    "interactions_dmp.csv",
    "interactions_eole_campagnes.csv",
    "interactions_eole_demandes.csv",
    "interactions_eole_leads.csv",
    "interactions_eole_opportunites.csv",
    "interactions_eole_taches.csv",
    "interactions_ged.csv"
]

for strg in FILE_NAME:

    with open("/Users/fox/Documents/TX/Interactions/" + strg, "r", encoding="Latin-1") as csvFile:
        csvReader = csv.reader(csvFile)

        i = 0
        for row in csvReader:
            i += 1
        print("Read " + strg + " with " + str(i) + " entry.")




