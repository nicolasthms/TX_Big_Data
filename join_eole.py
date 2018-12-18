import csv
import pandas
import random
import numpy as np
from sklearn.cluster import KMeans

def importDataset(strg):
    with open("/Users/nicolas/downloads/TPE_UTT_Documents_Sources/interactions/" + strg, "r", encoding="Latin-1") as csvFile:
        csvReader = csv.reader(csvFile, delimiter = ';', quotechar = '"')
        i = 0
        tab = []
        col = ""
        for row in csvReader:
            if (len(col)<1) :
                col = row
            else:
                tab.append(row)
                i += 1
        print("Read " + strg + " with " + str(i) + " entry.")
        result = dict()


        for i in range(len(col)):
            frame = []
            for row in tab:
                frame.append(row[i])
            result[str(col[i])] = frame


    return result

camp = importDataset("interactions_eole_campagnes.csv")
dem = importDataset("interactions_eole_demandes.csv")

campPD = pandas.DataFrame(data = camp)
demPD = pandas.DataFrame(data = dem)


### Inner join on #ID_Client
join = pandas.merge(campPD, demPD, 'inner', "#ID_CLIENT")
#print(join)

### Join column headers
# print(list(join))

num = 0

NB_RANDOM_ROWS = 10
NB_CLIENT_ENTRY_MIN = 20

### Make a list of random rows id
for k in random.sample(range(0, join.shape[0]), NB_RANDOM_ROWS):

    ### Select from that random row ID all the dataframe entrys for this client
    client = join.loc[join['#ID_CLIENT'] == str(join.at[k, "#ID_CLIENT"])]
    #pandas.set_option('display.max_columns', None)
    #print(unePersonne)

    ### Make sure there's enough entry for that client
    if client.shape[0] > NB_CLIENT_ENTRY_MIN :
        num += 1

        clientDate = client.loc[:, "HORODATE_x"]
        npClient = clientDate.as_matrix()
        km = KMeans(n_clusters=3).fit(npClient)

print(num)
