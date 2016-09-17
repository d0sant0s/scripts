# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = 100
epsilon = 0.1
high = x
low = 0
y = int((high + low)/2)

print("Please think of a number between 0 and 100!")
while abs(y - x) >= epsilon:    
    print("Is your secret number " + str(y) + "?")
    guess = input("Enter 'h' to indicate the guess is too high. \
    Enter 'l' to indicate the guess is too low. \
    Enter 'c' to indicate I guessed correctly. ")
    if guess == 'h':
        high = y
        y = int((high + low)/2.0)
    elif guess == 'l':
        low = y
        y = int((high + low)/2.0)
    elif guess == 'c':
        print('Game over. Your secret number was: ', y)
        break
    else:
        print("Does not compute. Beep boob beep. Try again.")