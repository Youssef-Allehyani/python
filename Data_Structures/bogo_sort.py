import sys
import random
from load import load_numbers

def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
    return True   
def bogo_sort(values):
    a = 0
    while not is_sorted(values):
        print(a)
        random.shuffle(values)
        a +=1
    return values             


print(bogo_sort(load_numbers('Data_Structures/Files/numers.txt')))       