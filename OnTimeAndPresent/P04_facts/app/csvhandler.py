# FACts - Deven Maheshwari, Aaron Contreras, Oscar Wang, Owen Yaggy
# Softdev
# P04 - Le Fin
# 2022-06-10

from black import main
import pandas as pd
import csv
import sys

# reads csv or excel file then returns a dataframe
def read_file(file_name):
    if file_name.endswith('.csv'):
        df = pd.read_csv(file_name)
    elif file_name.endswith('.xlsx'):
        df = pd.read_excel(file_name)
    else:
        print("File type not supported")
        return None
    return df

def get_headers(filename):
    fields = []
    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return fields
        
    # Testing
    print("Total no. of rows: %d"%(csvreader.line_num))
    print('Field names are:' + ', '.join(field for field in fields))
    print('\nFirst 5 rows are:\n')
    for row in rows[:5]:
        # parsing each column of a row
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')

def get_fields(filename, col):
    helper = [col]
    df = pd.read_csv(filename, usecols=helper)
    return df


def main():
    return 1

if __name__ == "__main__":
    main()