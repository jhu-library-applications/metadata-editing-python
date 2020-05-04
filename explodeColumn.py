import pandas as pd
import argparse
from datetime import datetime

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
    columnName = input('Enter column to explode: ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

df_1 = pd.read_csv(filename, header=0)
df = df_1[['bib', columnName]].copy()
df[columnName] = df[columnName].str.split('|')
df.reset_index()
df = df.explode(columnName)

print(df.columns)
print(df.head)
df.to_csv(path_or_buf=columnName+'Exploded_'+dt+'.csv')
