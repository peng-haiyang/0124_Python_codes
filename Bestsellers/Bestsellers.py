print ("************" * 1)
print ("Draw A US flag")
print ("************\n" * 1)

import math
import turtle
import tkinter
import re


#### Define function ###
def initial():
    print("\nWhat would you like to do?")
    print("1. Look up year range")
    print("2. Look up month/year")
    print("3. Search for author")
    print("4. Search for title")
    print("Q. Quit")
    manu_list = [1,2,3,4,'Q']
    return(input())

results = []
with open('Books_list.txt') as ipf:
    for line in ipf:
        results.append(line.strip().split('\t'))

## Look up year range ##
def search_yr(begin,end):
    i = 1
    print("\nAll article(s) between %d and %d:\n" % (begin, end))
    for list in results:
        word = list[3]
        if int(word[-4:]) >= begin and int(word[-4:]) <= end:
            print("\t%s, by %s (%s)" % (list[0], list[1], list[3]))
            i = 0 ## justify if any result found
            continue
    if i == 1:
        print("Sorry, no result found, please try again\n")

## Look up month/year ##
def search_my(month,year):
    i = 1
    print("\nAll article(s) in month %d of %d:\n" % (month, year))
    for list in results:
        word = []
        word_temp = list[3]
        word = word_temp.split('/')
        if int(word[0]) == month and int(word[2]) == year:
            print("\t%s, by %s (%s)" % (list[0], list[1], list[3]))
            i = 0 ## justify if any result found
            continue
    if i == 1:
        print("Sorry, no result found, please try again\n")

## Search for author ##
def search_at(srh):
    i = 1
    print("\nAll article(s) by %s:\n" % srh)
    for list in results:
        word = list[1]
        if srh.lower() in word.lower():
            print("\t%s, by %s (%s)" % (list[0], list[1], list[3]))
            i = 0 ## justify if any result found
            continue
    if i == 1:
        print("Sorry, no result found, please try again\n")

## Search for title ##
def search_ti(srh):
    i = 1
    print("\nAll article(s) titled: %s\n" % srh)
    for list in results:
        word = list[0]
        if srh.lower() in word.lower():
            print("\t%s, by %s (%s)" % (list[0], list[1], list[3]))
            i = 0 ## justify if any result found
            continue
    if i == 1:
        print("Sorry, no result found, please try again\n")

#### Function Definition Finished###

while True:
    ip = initial()
    if ip == '1':
        begin = int(input("Please enter beginning year (as a number):"))
        end = int(input("Please enter ending year (as a numer):"))
        search_yr(begin,end)
        continue
    if ip == '2':
        month = int(input("Please enter ending month (as a number 1-12):"))
        year = int(input("Please enter ending year (as a number):"))
        search_my(month,year)
        continue
    if ip == '3':
        srch = input("please enter the author name:")
        search_at(str(srch))
        continue
    if ip == '4':
        srch = input("please enter the title:")
        search_ti(str(srch))
        continue
    if ip.upper() == 'Q':
        break
    else:
        print("Invalid input, please check the input manu again.")



