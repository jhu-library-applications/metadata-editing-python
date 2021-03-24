import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--column1')
parser.add_argument('-c2', '--column2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.column1:
    column1 = args.column1
else:
    column1 = input('Enter identifier column: ')
if args.column2:
    column2 = args.column2
else:
    column2 = input('Enter column to count values: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df = pd.read_csv(filename, header=0)

allItems = []
for count, row in df.iterrows():
    row = row
    id = row[column1]
    values = row[column2]
    values = str(values).split('|')
    total_values = len(set(values))
    row['total_values'] = total_values
    allItems.append(row)

updated_df = pd.DataFrame.from_dict(allItems)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
updated_df.to_csv('totalValuesOf'+column2+'_'+dt+'.csv')
