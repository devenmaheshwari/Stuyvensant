# Umlauts - Yusuf Elsharawy & Bill, Alejandro Alonso & Señor Juan, Deven Maheshwari & Batman Pd. 1
# SoftDev
# K10 -- Prints a weighted-random job read from a CSV file containing names & percentages
# 2021-09-28

# POW-WOW SUMMARY
# We decided to use the csv module because it's robust and easy to use.
# Alejandro directed us towards using a DictReader and started the file-reading code.
# We then determined how a job could be chosen with weightde probability
# and implemented the algorithm we came up with. After separating our code
# into functions, we just had to clean things up and add comments.
# DISCOVERIES
# I (re-)discovered DictReader from the csv module.
# I can't remember the last time I read a csv file in Python,
# so it was a nice refresher.
# QUESTIONS - N/A
# COMMENTS
# Picking the weighted random job would be faster with a binary search
# & pre-constructed cumulative percentages, but for this purpose it may
# not be worth the extra programmer time & code complexity.

import csv, random
from collections import defaultdict
import os

jobPercentages = {}

# Initializes data from file
def init():
    global totalPercentage
    with open('occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row["Job Class"]
            percentage = float(row["Percentage"])
            jobPercentages[job] = percentage

    totalPercentage = jobPercentages['Total']
    jobPercentages['Other'] = 100 - totalPercentage
    del jobPercentages['Total']

# Returns an occupation with weighted probability
def chooseRandom():     #
    randVal = random.uniform(0, 100) # randomly chooses a number from 0 to total percentage
    for k, v in jobPercentages.items():
        randVal -= v
        if randVal <= 0:    # first cumulative percentage >= random value is the job chosen
            return k

# Test to ensure that the probabilities really do match up
def test():
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
    # test() # Uncomment to run tests
