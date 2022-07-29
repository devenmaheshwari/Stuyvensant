# Deven Maheshwari
# SoftDev
# Write Name / Intro to Python / Randomly chooses a student from pd. 1 and pd. 2 and prints their name
# 2021-09-21
#

import random

pd1 = ["Alejandro Alonso", "Yusuf Elsharawy", "Deven Maheshwari"]
pd2 = ["Fake Name1", "Fake Name2", "Fake Name3"]

def writeName():
    period = random.randint(0,1)
    if (period):
        index = random.randint(0,len(pd1)-1)
        print(pd1[index])
    else:
        index = random.randint(0, len(pd2)-1)
        print(pd2[index])
    
writeName()
