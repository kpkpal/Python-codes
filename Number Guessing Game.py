# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:26:52 2019

@author: KPK
"""
def main():
    import random
    number = random.randint(1,10)
    tries = 1
    
    question = input("Hello Welcome to Number Guessing Game. \nWould you like to play a Game? [Y / N] \nYour Choice: ").lower()
    if question == "n":
        print ("Thank you for choosing to play Number Guessing Game. Have a Nice Day")
        
    if question == "y":
        uname = input("Hello. Please input a User Name: ")
        print("Hello " '"' + uname + '"' " I'm thinking of a number between 1 & 10. \nPlease make a Guess")
        guess = int(input("Your Guess: "))
        if guess != number:
            tries +=1   
            guess = int(input("Try Again: "))
        if guess < number:
            print("No Cheating. Guess a Higher Value Number")
        if guess > number:
            print("Thats too big a number for me to handle. C'mon, Guess a Lower Value Number")
    
        while guess == number:
            print ("\nYou got it right, Great! \nThe number I guessed was",'"', str(int(number)),'"', '\n'"Your total No of tries: ", str(int(tries)))
            
            restart = input("Do you want to start again? [y / n]").lower()
            if restart == "y":
                main()
            else:
                print ("Thank you for choosing to play Number Guessing Game. Have a Nice Day")
        
        