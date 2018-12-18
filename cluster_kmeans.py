import csv
import pandas
import random
import numpy as np
from sklearn.cluster import KMeans
import datetime as dt
import matplotlib.pyplot as plt

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

def changeDateFormat(d):
    nst = str(d).split('.')
    date = dt.datetime.fromisoformat(nst[0])
    return date.toordinal()

camp = importDataset("interactions_eole_campagnes.csv")
dem = importDataset("interactions_eole_demandes.csv")

campPD = pandas.DataFrame(data = camp)
campPD['document_type'] = 1
demPD = pandas.DataFrame(data = dem)
demPD['document_type'] = 1

#join = pandas.concat([campPD, demPD])

join = campPD.append(demPD, ignore_index= True)

pandas.set_option('display.max_columns', None)
print(join.shape)


num = 0


### Parameters
NB_RANDOM_ROWS = 30
NB_CLIENT_ENTRY_MIN = 6

pattern = []

### Make a list of random rows id
for k in random.sample(range(0, join.shape[0]), NB_RANDOM_ROWS):
    #print(join.at[k, "#ID_CLIENT"])


    ### Select from that random row ID all the dataframe entrys for this client
    client = join.loc[join['#ID_CLIENT'] == str(join.at[k, "#ID_CLIENT"])]

    ### Display client informations
    # pandas.set_option('display.max_columns', None)
    # print(client)

    ### Make sure there's enough entry for that client
    if client.shape[0] > NB_CLIENT_ENTRY_MIN :
        num += 1
        clientDate = client[["HORODATE", "document_type"]]

        clientDate.loc[:, "HORODATE"] = clientDate.loc[:, "HORODATE"].apply(changeDateFormat)

        clientKM = clientDate.as_matrix()

        km = KMeans(n_clusters=3).fit(clientKM)

        clusters = km.labels_
        centers = km.cluster_centers_

        client['cluster'] = clusters

        for ncluster in range(0, len(centers)):
            aCluster = client.loc[client['cluster'] == ncluster].as_matrix()
            clusterContent = []
            for jcluster in range(0, len(aCluster)):
                canal = aCluster[jcluster][1]
                motif = aCluster[jcluster][2]
                type_contact = aCluster[jcluster][5]
                clusterContent.append(str(canal) + " " + str(motif) + " " + str(type_contact))
            pattern.append(clusterContent)



print(num)

for rowpat1 in pattern:
    print(rowpat1)