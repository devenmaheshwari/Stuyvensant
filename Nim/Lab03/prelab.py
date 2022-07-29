# Deven Maheshwari
# March 22, 2022
# Cybersecurity
# Lab 03 Prelab

def task01():
    a = [65,66,97,98,10,72,101,108,108,111,32,119,111,114,108,100,10]
    with open("test.txt", 'wb') as f:
        for i in a:
            f.write(i.to_bytes(1,byteorder='big'))

    return a

def task02():
    a = []
    with open("test.txt", 'rb') as f:
        while (b := f.read(1)):
            x = int.from_bytes(b,byteorder='big')
            x += 1
            b = x.to_bytes(1, byteorder='big')    
            a.append(b)
        
    with open("test2.txt", 'wb') as f:
        for i in a:
            f.write(i)
    return a


def main():
    print(task01())
    print(task02())

if __name__ == "__main__":
    main()