import csv

# Made by Ben Mills - 07/2020

# Available export formats
availableExportFormats = ['Capture', 'MA3D']
# Chosen export format
exportFormat = ['Capture']

# iData = Instrument Data
filename = 'RotationTest.txt'
iDataFile = open(filename)
iData = csv.DictReader(iDataFile, dialect='excel-tab')
newIData = list(iData)


# Main Function
def runExport():
    if exportFormat == ['Capture']:
        print('Chosen export format:', ''.join(exportFormat), '\n')
        for row in newIData:
            # Make data numeric
            global X,Y,Z
            X = float(row['X Rotation'])
            Y = float(row['Y Rotation'])
            Z = float(row['Z Rotation'])
            print(row['Instrument Type'], '/ U:', row['Unit Number'], 'on the', row['Position'], '\n- WAS at rotation:      ', X, '/', Y, '/', Z)

            # Data Manipulation
            X = X+45
            Y = Y+45
            Z = Z+45
            X,Y,Z = X,Z,Y

            row['X Rotation'] = X
            row['Y Rotation'] = Y
            row['Z Rotation'] = Z
            print('- IS NOW at rotation:   ', X, '/', Y, '/', Z, '\n')

    elif exportFormat == ['MA3D']:
        print('Chosen export format:', ''.join(exportFormat), '\n')
        print('This export format is currently unsupported.')
    else:
        print('Invalid export format chosen.')

runExport()

# File Export
splitFile = filename.split('.', 1)[0]
saveFilename = (''.join(splitFile), ' - for ', ''.join(exportFormat), '.txt')
print('Exported to: ', ''.join(saveFilename))


with open(''.join(saveFilename), 'w', newline='') as csvfile:
    fieldnames = newIData[1]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel-tab')

    writer.writeheader()
    writer.writerows(newIData)

iDataFile.close()
