# Deven Maheshwari
# March 24, 2022
# Cybersecurity
# Lab 03 1.1

import sys

def hexdump(filename):
    with open(filename, 'rb') as f:
        b = f.read()
        result = hex(int.from_bytes(b,byteorder='big'))
    result = str(result)[2:]
    answer = ''
    count = 0
    for i in result:
        answer += i
        count += 1
        if count % 2 == 0:
            answer += " "
            count = 0
    return answer

def main():
    print(hexdump(sys.argv[1]))

if __name__ == "__main__":
    main()