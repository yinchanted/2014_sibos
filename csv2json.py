import csv
import json
csvfile = open('streams_2015.csv')
csvReader = csv.reader(csvfile)
csvData = list(csvReader)
print csvData
links = []
for i in range(1, (len(csvData))):
    for j in range(1, (len(csvData[i]))):
        if (csvData[i][j] != ''):
            links += {"source":csvData[i][0], "target":csvData[0][j], "value":csvData[i][j]}, 
nodes = []
for x in range(1, (len(csvData))):
    nodes += {"name":csvData[x][0]},
for y in range(1, (len(csvData[i]))):
    nodes += {"name":csvData[0][y]},
jsonData = {"links": links, "nodes": nodes}
with open('jsonData.json', 'w') as f:
     json.dump(jsonData, f)