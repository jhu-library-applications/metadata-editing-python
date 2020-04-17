import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

columnName = input('Enter columnName: ')

df = pd.read_csv(filename)
unique = df[columnName].unique()
print(unique)
for value in unique:
    newDF = df.loc[df[columnName] == value]
    print(newDF)
    newDF.to_csv(path_or_buf=value+'.csv', index=False)
