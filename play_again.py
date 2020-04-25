"""
Created on 4/25/2020

@author: erosales

Description of file: 
"""
import os
import sys

from clear_log import clear

valid_answers = ['yes', 'no']

#TODO does not work
def play_again():
    print("\nWould you like to play again?")
    again = input("Please type in \"Yes\" or \"No\": ")
    clear()

    if again.lower() == 'yes':
        os.execl(sys.executable, sys.executable, *sys.argv)

    elif again.lower() == 'no':
        exit()
    else:
        while again.lower() not in valid_answers:
            print("\nWhoops! you typed in \"%s\"." % again)
            again = input("Please type in \"Yes\" or \"No\": ")
            clear()