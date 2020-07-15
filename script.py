import csv

runesSourceFile = open('Runes.txt', 'r')
runesCsvFile = open('runes.csv', 'w', newline='')
writer = csv.writer(runesCsvFile, delimiter='|', quoting=csv.QUOTE_NONE)

for line in runesSourceFile:
    modifiedLine = line.replace('\t', ',').strip()
    writer.writerow([modifiedLine])

runesCsvFile.close()