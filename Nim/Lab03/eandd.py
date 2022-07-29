# Deven Maheshwari
# March 24, 2022
# Cybersecurity
# Lab 03 1.2/1.3

import sys

def encode(textfile, keyfile, ciphertextfile):
    a = []
    with open(textfile, 'rb') as f:
        while (b := f.read(1)):
            x = int.from_bytes(b,byteorder='big')
            x += 1
            b = x.to_bytes(1, byteorder='big')    
            a.append(b)
        
    with open(ciphertextfile, 'wb') as f:
        for i in a:
            f.write(i)

def decode(ciphertextfile, keyfile):
    a = []
    with open(ciphertextfile, 'rb') as f:
        while (b := f.read(1)):
            x = int.from_bytes(b,byteorder='big')
            x -= 1
            b = x.to_bytes(1, byteorder='big')    
            a.append(b)
    
    with open("helper.txt", 'wb') as f:
        for i in a:
            f.write(i)
    
    with open("helper.txt", 'rb') as f:
        b = f.read()
        
    return b

def xor(plaintext, keytext):
    a = []

    with open(plaintext, 'rb') as f, open(keytext, 'rb') as g:
        plain = f.read()
        key = g.read()

        for i in range(len(plain) - len(key)):
            key += key[i]
        
        for i in range(len(plain)):
            if plain[i] != key[i]:
                a.append(1)
            else:
                a.append(0)
        
    answer = ''
    for i in a:
        answer += str(i)
    
    return answer


def main():
    try:
        if (sys.argv[1] == '-e'):
            encode(sys.argv[2], sys.argv[3], sys.argv[4])
        elif (sys.argv[1] == '-d'):
            print(decode(sys.argv[2], sys.argv[3]))
        elif (sys.argv[1] == '-x'):
            print(decode(sys.argv[2], sys.argv[3]))
    except:
        print("Incorrect Arguments")

if __name__ == "__main__":
    main()