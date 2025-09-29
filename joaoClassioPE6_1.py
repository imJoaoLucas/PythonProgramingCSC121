#Joao Classio 09/28/2025 joaoClassioPE6_1.py
'''
This is a progam that receives how many random numbers to be created and write these number 
in a file. After that, read this file and display; All the number in a single output line, 
the sum of all numbers, the avarage, largest and smallest.
'''
import random

def createFile():
    '''
    This function generates a file containing random integer values between 1 and 1000
    in the current directory with the name "myfile.txt". It return the number choosen 
    by the user that represents how many values there are in the file
    '''
    userEntry = int(input("How many random number should the program write? "))
    
    with open('myfile.txt', 'w') as inputFile: #Used to open the file and creates a file object(inputFile)
        for i in range(userEntry):
            inputFile.writelines(str(random.randint(1,1000)) + "\n")
    print("File created")
    
    return userEntry

def readFile():
    '''
    This function displays the numbers in the file 
    '''
    with open('myfile.txt', 'r') as file:
        line = file.read().replace("\n", " ") #Replaces the broken line symbol with a blank space
        print(line)

def sumFile():
    '''
    This function displays the sum of the numbers contained within the file and
    also returns this value as an integer
    '''
    with open('myfile.txt', 'r') as file:
        line = file.readline()
        total = 0
        while line != "":
            total = total + int(line)
            line = file.readline()
        print(f"\nThe sum of the numbers is = {total}")
        return total

def avarageFile(total, numOcurrence):
    '''
    This function displays the avarage of this numbers
    '''
    print(f"\nThe avarage of these {numOcurrence} numbers is = {total / numOcurrence: .2f}")
     
def maxMinFile():
    '''
    This function compares the values in order to display the lowest and the highest
    '''
    highestValue = 0 
    lowestValue = 1000 #The max for the range on ramdon numbers generator
    with open('myfile.txt') as file:
        for line in file:
            currentValue = int(line.strip())
            if currentValue > highestValue:
                highestValue = currentValue
            if currentValue < lowestValue:
                lowestValue = currentValue
        print(f"\nThe highest value is = {highestValue} and the lowest is = {lowestValue}")

def main(): #The main method used to call all methods and run a replay loop
    again = "y"
    while again.lower() == "y":
        randomNumbers = createFile()
        readFile()                  
        total = sumFile()
        avarageFile(total, randomNumbers)
        maxMinFile()        
        again = input("\n\nWhant to run it again? Y = continue | ENTER = exit ")

main()     