# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:29:40 2019

@author: KPK
"""

import random
x = (1)
y = (10)
number = random.randint(x,y)
tries = 1

while 1:
    question = input("Hello Welcome to the 'Number Guessing Game'. \nWould you like to play the Number Guessing Game? [Y / N] \nYour Choice: ").lower()
    if question == "n": 
        print ("\nThank you for choosing to play Number Guessing Game. Have a Nice Day")
        break
    
    if question == "y":
        uname = input("Hello. Please input a User Name: ")
        print("Hello " '"' + uname + '"' " I'm thinking of a number between 1 to 10. \nPlease make a Guess")
        
        while 2:
            guess = int(input(""))
            
            if guess < x:
                print("Oh no. No Cheating. Guess a number larger than",str(int(x)))
                
            if guess > y:
                print("Thats too big a number for me to think. C'mon, guess something less than",str(int(y)))
                
            if guess != number:
                print("Please try Again: ")
                tries +=1
            
            if guess == number:
                print ("\nYou got it right, Great! \nThe number I guessed was",'"', str(int(number)),'"', '\n'"Your total No of tries: ", str(int(tries)))
                break
            
            
                
         

        



   
    
        