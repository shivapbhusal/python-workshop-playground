#This programs takes two positive integers as the user inputs, and generates random numbers between those two integers. 
from random import *
num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
def generateRandom(a, b):
    randomnum=randint(int(num1),int(num2))
    print(randomnum)
    user_decision=input("do you want to roll again ? y or n")
    if user_decision=='y':
        generateRandom(num1,num2)
    else:
        print("your game has ended")

generateRandom(num1, num2)





