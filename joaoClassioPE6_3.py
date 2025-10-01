#Joao Classio 10/01/2025 joaoClassioPE6_3
'''
This program will open a file, countaining numbers and calculate the avarage. Also
suited with error handlers in case of IOError in case of a problem with the file and ValueError
if there is a non-numeric value in the file.
'''
FILE_NAME = "exceptionNumbers.txt" #A constant with the file name, works well to a file opening program 
def avarageCalculator(): #Function that calculates the avarage in the file
    with open(FILE_NAME, 'r') as file:
        total = 0
        count = 0
        for line in file:
            try: #Try to convert the line without the \n into a integer 
                total += int(line.strip())
            except ValueError: #Print the non-numeric value found in the list
                print(f'There is a string "{line.strip()}" in your number list')
            count += 1
        return total / count    
                
def main(): #The main making the program keep runing and calling the avarageCalculator method
    again = "y"
    while again.lower() == "y":
        print(f'The avarage in this file is = {avarageCalculator():.2f}')
        again = input("\nDo you want to run it again? Y = again / ENTER = exit ")
                 
try: #Try to run the main, if there is no error with the file
    main()
except IOError: #If there is an error with the file, it will print "File not found" and the file name
    print(f'File "{FILE_NAME}" not found')