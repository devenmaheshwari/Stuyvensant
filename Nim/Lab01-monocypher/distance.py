# Deven Maheshwari
# March 1, 2022
# Cybersecurity
# Lab 01 Part 1.2 

import math
import sys
import frequency

def distance(base, unknown):
    """ Write a program that when given unknown text, and a baseline text calculate the distance between two different sets of letter frequencies.
    
    Returns: 
        Given text1 has frequencies [0.2, 0.2, 0.2, 0.2] and text2 has frequencies [0.2, 0.25, 0.06, 0.29]
        The distance is sqrt ( (.2 - .2) 2 + (.2 - .25) 2 + (.2 - .06) 2 + (.2 - .29) 2 )
        The result of which is sqrt(0.0302), so the distance is: 0.173781
    """

    # Base Text
    basedict = frequency.letter_frequency(base)
    unknowndict = frequency.letter_frequency(unknown)

    sum = 0
    for index in basedict:
        sum += euclidean_helper(basedict[index], unknowndict[index])

    return sum

def euclidean_helper(a, b):
    return (a-b) ** 2

def main():
    try: 
        print(distance(sys.argv[1], sys.argv[2]))
    except:
        print("Not sufficient arguments")

if __name__ == "__main__":
    main()