# Deven Maheshwari
# March 1, 2022
# Cybersecurity
# Lab 01 Part 1.1 

import sys

def letter_frequency(filename):
    """ Write a program that when given source text, uses that text to analyze letter frequency.
    
    Assumptions: 
        Letter frequency should ignore case (both lower and uppercase are counted), and punctuation/special characters are completely discarded from the calculationss. The denominator of the frequency should be the total number of letters.
        Assume the text uses the English alphabet to simplify our programs.
    
    Returns: 
        Print out each letter and the frequency in the format:
            A 0.0452
            B 0.0023
            C 0.0013
            D 0.00024
            ...
            X 0.0
            Y 0.0005
            Z 0.0003 
    """
    letters = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 
        'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
        'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0,
        'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
        'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0,
        'Z': 0
    }

    file = open(filename, 'r')
    text = file.read()
    file.close()
    text = text.upper()
    
    total = 0; 

    for c in text:
        if c in letters.keys():
            total += 1 
            letters[c] += 1
    
    for i in letters.keys():
        letters[i] = letters[i] / total

    return letters

def main():
    try: 
        print(letter_frequency(sys.argv[1]))
    except:
        print("Not sufficient arguments")

if __name__ == "__main__":
    main()