# Deven Maheshwari
# March 9, 2022
# Cybersecurity
# Lab 02 

# This could be a lot cleaner

import string 
import sys
import decoding, distance

def encode(cleartext, keyfile):
    plaintext = open(cleartext, 'r').read().upper()
    key = open(keyfile, 'r').read().upper()

    for i in plaintext:
        if not i.isalpha():
            plaintext = plaintext.replace(i, "")

    if len(key) > len(plaintext):
        key = key[ :len(plaintext)]
    elif len(key) < len(plaintext):
        j = 0
        for i in range(len(plaintext) - len(key)):
            key += key[j]
            j += 1 
            if j > len(key):
                j = 0

    final = shift(plaintext, key, code = True)

    return final

def decode(ciphertext, keyfile):
    plaintext = open(ciphertext, 'r').read().upper()
    key = open(keyfile, 'r').read().upper()

    for i in plaintext:
        if not i.isalpha():
            plaintext = plaintext.replace(i, "")

    if len(key) > len(plaintext):
        key = key[ :len(plaintext)]
    elif len(key) < len(plaintext):
        j = 0
        for i in range(len(plaintext) - len(key)):
            key += key[j]
            j += 1 
            if j > len(key):
                j = 0

    final = shift(plaintext, key, code = False)

    return final

def shift(plaintext, key, code):
    letters = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 
        'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
        'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
        'Z': 25
    }
    if code:
        k = 1
    else:
        k = -1
    for i in letters.keys():
        letters[i] = letters.get(i) * k

    result = ""
    for i in range(len(plaintext)):
        if plaintext[i] in letters.keys():
            if (65 <= ord(plaintext[i]) + letters.get(key[i]) <= 90): 
                result += chr(ord(plaintext[i]) + letters.get(key[i]))  
            else:
                result += chr(ord(plaintext[i]) + letters.get(key[i]) - (k * 26))
    
    return result

def cracker(ciphertext, n):
    smallest = sys.maxsize
    answer = ""
    keylength = n

    for p in range(1,n+1):
        cipher = open(ciphertext, 'r').read()
        text_list = []

        for i in range(p):
            text_list.append("")

        for i in range(len(cipher)):
            text_list[i % p] += cipher[i]
        
        for i in range(len(text_list)):
            text_list[i] = decoding.decipher(text_list[i])

        result = ""

        for j in range(len(text_list[p-1])):
            for i in range(len(text_list)):
                result += text_list[i][j] 
        
        for j in range(len(text_list)):
            if len(text_list[j]) > len(text_list[p-1]): 
                result += text_list[j][-1]
        
        if distance.distance(result) < smallest:
            smallest = distance.distance(result)
            answer = result
            keylength = p

    return answer, keylength

def guesskeylength(ciphertext, n):
    return cracker(ciphertext, n)[1]


def main():
    try:
        if (sys.argv[1] == '-e'):
            print(encode(sys.argv[2], sys.argv[3]))
        elif (sys.argv[1] == '-d'):
            print(decode(sys.argv[2], sys.argv[3]))
        elif (sys.argv[1] == '-c'):
            print(cracker(sys.argv[2], 16)[0])
        elif (sys.argv[1] == '-g'):
            print(guesskeylength(sys.argv[2], 16))
    except:
        print("Incorrect Arguments")


if __name__ == "__main__":
    main()