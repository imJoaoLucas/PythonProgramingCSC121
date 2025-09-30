#Joao Classio 09/30/2025 joaoClassioPE6_2
'''
This program is a basic input tester, it receives an entry of any value and tells 
the user if the entry is a number or not.
'''

def inputData(): #Imput method, it returns the string the user enter
    string = input("Input anything, I will test for a number OR press 'enter' to exit ")
    return string

def numTest(string): #The function that will test the value, using try. 
    '''
    It try to perform a basic float conversion (if it's an integer, it will be
    converted with no proble, if it's a float, it will not convert neither result
    in an error. Otherwise, if in some case(if the entry is not only numbers) it
    fails and the ValueError happend when trying to convert, the program will say
    that the entry is not a number.
    '''
    try:
        s = float(string) + 7.77
        print(f"Your entry '{string}' is a number")
    except ValueError:
        print(f"Your entry '{string}' is not a number")

def main(): #The main method calling all other methods
    string = inputData()
    
    while string != "":
        if string != '':
            numTest(string)
        string = inputData()
        
main() 