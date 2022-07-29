# Deven Maheshwari
# March 2, 2022
# Cybersecurity
# Lab 01 Part 1.3

import sys
import math
import distance

def decipher(ciphered):
    """Analyzes letter frequency contained in a ceaser shifted file, and deocdes the message automatically. 
    
    Arguments:
        Ciphertext filename

    Returns:
        Printing a single decodede message.
    """

    min_position_f = 0
    min_position_r = 0
    min_distance_forward = distance.distance(ciphered, 'alice.txt')
    min_distance_reversed = distance.distance(ciphered, 'alice.txt')

    for i in range(26): 
        f_shift(ciphered, i)
        temp = "filehelp.txt"
        if (min_distance_forward > distance.distance(temp, 'alice.txt')):
            min_distance_forward = distance.distance(temp, 'alice.txt')
            min_position_f = i
    
    for i in range(26): 
        r_shift(ciphered, i)
        temp = "filehelp.txt"
        if (min_distance_reversed > distance.distance(temp, 'alice.txt')):
            min_distance_reversed = distance.distance(temp, 'alice.txt')
            min_position_r = i
        
    if (min_distance_forward < min_distance_reversed):
        f_shift(ciphered, min_position_f)
    else:
        r_shift(ciphered, min_position_r)
    
    answer = "filehelp.txt"
    file = open(answer, 'r')
    text = file.read()
    file.close()

    return text

def f_shift(filename, n): 
    """Shifts letters contained in a string by a specified amount forward
    
    Arguments:
        filename - file to be shifted
        n - amount shifted (<= 26)
    
    Returns:
        result - string of shifted file contents
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
    text_helper = text.upper()
    file.close()

    result = ""
    
    for i in range(len(text_helper)):
        if text_helper[i] in letters.keys():
            if (65 <= ord(text_helper[i]) + n <= 90): 
                result += chr(ord(text[i]) + n)    
            else:
                result += chr(ord(text[i]) + n - 26)
        else:
            result += text[i]
    
    f = open("filehelp.txt", "w")
    f.write(result)
    f.close()

def r_shift(filename, n): 
    """Shifts letters contained in a string by a specified amount reversed
    
    Arguments:
        filename - file to be shifted
        n - amount shifted (<= 26)
    
    Returns:
        result - string of shifted file contents
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
    text_helper = text.upper()
    file.close()

    result = ""
    
    for i in range(len(text_helper)):
        if text_helper[i] in letters.keys():
            if (65 <= 155 - ord(text_helper[i]) + n <= 90): 
                if (97 <= ord(text[i]) <= 122):
                    result += chr(219 - ord(text[i]) + n)
                else:
                    result += chr(155 - ord(text[i]) + n)    
            else:
                if (97 <= ord(text[i]) <= 122):
                    result += chr(219 - ord(text[i]) + n - 26)
                else:
                    result += chr(255 - ord(text[i]) + n - 26)    
        else:
            result += text[i]
    
    f = open("filehelp.txt", "w")
    f.write(result)
    f.close()


def main():
    print(decipher(sys.argv[1]))

if __name__ == "__main__":
    main()