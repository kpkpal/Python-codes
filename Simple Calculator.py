# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:28:10 2019

@author: KPK
"""

''' My Simple calculator program: '''

def loop():
    while True:
        option = input ("Welcome to My Simple Calculator using Python \n Please select one of the following options \n Press 1 for Addition \n Press 2 for Subtraction \n Press 3 for Multiplication \n Press 4 for Division \n Press 5 for Exit \n Enter your option here:")
        if int (option) == 5:
            print("Thank you for using My Simple Calculator. Have a nice day")
            break
            
        num1 = input ("Enter the First Number:")
        num2 = input ("Enter the Second Number:")
      
        if int (option) == 1:
            print("Solution: " + str(int(num1)+int(num2)))
        elif int (option) == 2:
            print("Solution: " + str(int(num1)-int(num2)))
        elif int (option) == 3:
            print("Solution: " + str(int(num1)*int(num2)))
        else:
            int (option) == 4
            print("Solution: " + str(int(num1)/int(num2)))
            
    restart = input("Do you want to start again? [Y / N]").lower()
    if restart == "y":
        loop()
    else:
        exit()
            
#123
        