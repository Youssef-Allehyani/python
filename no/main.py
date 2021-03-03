# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import datetime
from colorama import Fore, Back, Style

def GCD(number3, number4):
    number1 = int(number3)
    number2 = int(number4)
    if (number2 > number1):
        timmper = number1
        number1 = number2
        number2 = timmper
    else:
        while (number2 != 0):
            temp = number2
            number2 = number1 % number2
            number1 = temp
    return number1


def run():
    while (True):
        try:
            number1 = input("enter the first number : ")
            if (number1.upper().__eq__("C")):
                break
            number2 = input("enter the second number : ")
            if (number2.upper().__eq__("C")):
                break
            t0 = time.time()
            TheGCD = GCD(number1, number2)
            time.sleep(1)
            t1 = time.time()
            nonosacand = t1 - t0
            print("GCD = " + str(TheGCD))
            print("time =" + str(nonosacand))
            print("=======================================")
            number1 = input("enter the first number: ")
            number2 = input("enter the second number: ")
            number3 = input("enter the third number: ")
            if (number3.upper().__eq__("C")):
                break
            t0 = datetime.datetime().now()
            TheGCD = GCD(number1, GCD(number2, number3))
            t1 = datetime.datetime().now()
            nonosacand = t1 - t0
            print("GCD = " + str(TheGCD))
            print("time =" + str(nonosacand.microseconds))
            print("=======================================")


        except ValueError:
            print( "please inter the number !!!!!")



if __name__ == '__main__':
    run()
