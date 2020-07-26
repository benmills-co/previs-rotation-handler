import csv

# Made by Ben Mills - 07/2020

# Available export formats
availableExportFormats = ['Capture', 'MA3D']
# Chosen export format
exportFormat = ['Capture']

file = 'Jess-TheVic.txt'
iDataFile = open(file)
iData = csv.DictReader(iDataFile, dialect='excel-tab')
newIData = []

# Main Function
def runExport():
    if exportFormat == ['Capture']:
        print('Chosen export format:', ''.join(exportFormat), '\n')
        for row in iData:
            # Make data numeric
            X = float(row['X Rotation'])
            Y = float(row['Y Rotation'])
            Z = float(row['Z Rotation'])
            print(row['Instrument Type'], '/ U:', row['Unit Number'], 'on the', row['Position'], '\n- WAS at rotation:      ', X, '/', Y, '/', Z)

            # Data Manipulation
            X = X+90
            Y = Y+90
            Z = Z+90
            X,Y,Z = X,Z,Y

            print('- IS NOW at rotation:   ', X, '/', Y, '/', Z, '\n')

    elif exportFormat == ['MA3D']:
        print('Chosen export format:', ''.join(exportFormat), '\n')
        print('This export format is currently unsupported.')
    else:
        print('Invalid export format chosen.')

runExport()

splitFile = file.split('.', 1)[0]
fileSaveName = (''.join(splitFile), ' - for ', ''.join(exportFormat), '.txt')
print(''.join(fileSaveName))


iDataFile.close()
