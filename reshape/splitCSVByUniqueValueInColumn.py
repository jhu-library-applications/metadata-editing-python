import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--columnName')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.columnName:
    columnName = args.columnName
else:
    columnName = input('Enter column to divide by value: ')

df = pd.read_csv(filename)
unique = df[columnName].unique()
print(unique)
for value in unique:
    newDF = df.loc[df[columnName] == value]
    print(newDF)
    value = value.replace('/', '-')
    newDF.to_csv(value+'.csv', index=False)
