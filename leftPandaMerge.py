import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
if args.file2:
    filename2 = args.file2
else:
    filename2 = input('Enter csv with marc data (including \'.csv\'): ')

df_1 = pd.read_csv(filename, header=0)
df_2 = pd.read_csv(filename2, header=0)

frame = pd.merge(df_1, df_2, how='left', on=['handle'], suffixes=('_1', '_2'))

print(frame.columns)
print(frame.head)
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
frame.to_csv(path_or_buf='mergedCSV_'+dt+'.csv')