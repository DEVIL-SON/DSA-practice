import random
import math

lower = int(input("Enter the lower number: "))
higher = int(input("Enter the higher number: "))

number = random.randint(lower, higher)

guess = int(input("Guess the Number: "))
while guess != number:      
    if (guess > number):
        print("Number is greater than the number you guessed!!")

    elif (guess < number):
        print("Number is lesser than the number you guessed!!")



# elif (guess == number):
print("Congrats!!! you guessed it RIGHT..")
