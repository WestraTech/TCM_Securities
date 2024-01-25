#Programmer: Gabriel Westra
#Program: Functions
#Date: 1.19.2024s

def nl(): #New Line Function
	print('\n')

def who_am_i(): #This is a funstion without parameters
	name = "Gabe" #Local variable
	age = 30
	print("My name",name,"and I am",age,"years old.")

who_am_i()

nl()

def addOneHundred(num):
	print(num + 100)
	
addOneHundred(1500) #1500 is the Argument which inserts itself into the Parameter

nl()

addOneHundred(0)

nl()

def add(x,y):
	print(x + y)

add(8,5)

nl()
