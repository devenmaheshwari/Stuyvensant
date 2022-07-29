# Deven Maheshwari
# SoftDev
# Write Name / Introduction to Python / Randomly chooses a student from pd. 1 and pd. 2 and prints their name
# 2021-09-27
#
# SUMMARY OF TRIO DISCUSSION
#   We went through each of our previous implementations of the WriteName funcition. All 3 of us used function calls and the random library, but Sadid's group also used an input method to ask the user to put in their name and period and catch any errors with that. 
# DISCOVERIES
#   We came across some issues when implementing. First, we were running in python 2 so that was a quick fix. We also noticed that our file was resetting the lists each time the functions were called so we added another input for the user to specify the action they want. Then we switched the lists to a dictonary with lists as the values for the period, as was specificed in the assignment. 
# QUESTIONS
#   Just in general, how was python2 changed to python3 (did it make it faster, better syntax, etc), and if it is not backwards compatable, why is it still considered python? 
# COMMENTS
#   None

import random

KREWES = {           # Dictonary for keeping nakes in a list for each period
    'pd1': [],
    'pd2': []
}

def addToList():     # Add name to a list 
    name = input("What is their name? ")
    period = int(input("What period is the student in? "))

    while period != 1 and period != 2:
        print("That is not a softdev period. Please input the information again.")
        period = int(input("What period is the student in? "))

    if period == 1:
        KREWES.get('pd1').append(name)
    else:
        KREWES.get('pd2').append(name)

    print(f"The student's name is {name} and their period is {period}.")

def printName():     # Prints random name in the dictonary
    all = KREWES.get('pd1') + KREWES.get('pd2')
    print (all[random.randrange(len(all))])

def main():
    while True:
        print('''
            1. Add a student
            2. Print out a random name
            3. Exit program
        ''')
        choice = input("Make a choice: ")
        if(choice != "1" and choice != "2" and choice != "3"):
            continue
        if(choice == "1"):
            addToList()
        if(choice == "2"):
            printName()
        if(choice == "3"):
            return
               
        

if __name__=="__main__":
    main()
