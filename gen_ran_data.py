import csv
import random
import time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.
    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

csvfile = open('Sibos_2014_random.csv')
csvReader = csv.reader(csvfile)
csvData = list(csvReader)

row = []
for i in range(1, (len(csvData))):
    if (i == 1):
        csvData[i-1][len(csvData[i-1])-1] = random.randint(3000,3200)
        csvData[i-1][len(csvData[i-1])-2] = randomDate("7/1/2014 1:30 PM", "10/2/2014 4:50 AM", random.random())
        csvData[i-1][len(csvData[i-1])-3] = randomDate("3/1/2014 1:30 PM", "7/1/2014 1:00 PM", random.random())
    elif (i != len(csvData)):
        if (csvData[i-1][0] != csvData[i-2][0]):
            csvData[i-1][len(csvData[i-1])-1] = random.randint(3000,3200)
            csvData[i-1][len(csvData[i-1])-2] = randomDate("7/1/2014 1:30 PM", "10/2/2014 4:50 AM", random.random())
            csvData[i-1][len(csvData[i-1])-3] = randomDate("3/1/2014 1:30 PM", "7/1/2014 1:00 PM", random.random())
print csvData

b = open('test.csv', 'w')
a = csv.writer(b)
a.writerows(csvData)
b.close()