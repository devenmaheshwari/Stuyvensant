# Umlauts - Deven Maheshwari, Alejandro Alonso, Yusuf Elsharawy Pd. 1
# SoftDev
# JobPercentages/Reading Files/Using the CSV library to read a file of occupations and percentages and choosing them according to weighted values. 
# 2021-09-28

import csv, random
from collections import defaultdict

jobPercentages = {}
totalPercentage = 100

def init():             # Reading CSV file
    global totalPercentage
    with open('occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row["Job Class"]
            percentage = float(row["Percentage"])
            if job == 'Total':
                totalPercentage = percentage
            else:
                jobPercentages[job] = float(percentage)

def chooseRandom():     # Choosing random value based on weighted percentages. 
    randVal = random.uniform(0, totalPercentage)
    for k, v in jobPercentages.items():
        randVal -= v
        if randVal <= 0:
            return k


def test():             # Testing to make sure weighted values are similar to percentages in given file
    numTrials = 10000
    numChosen = defaultdict(int)
    for i in range(numTrials):
        job = chooseRandom()
        numChosen[job] += 1
    for job, num in numChosen.items():
        print(job, 100*num/numTrials, sep='\t')

if __name__ == '__main__':
    init()
    print(chooseRandom())
    print()
    test()
