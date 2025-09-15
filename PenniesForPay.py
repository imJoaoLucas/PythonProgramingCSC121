# Joao L Classio 09/15/2025 PenniesForPay.py(PE4.1)
#This program will calculate the salary that doubles every day starting in 1 cent.

#Declaring variables and constants
again = "Y"

#Input Prompt
print("This program will calculate the salary that doubles every day starting in 1 cent.")

#Calculation
while again.lower() == "y":
    daysWork = int(input("\nEnter the number of days to calculate the salary: "))

    dailySalary = 0.01 #Set the values for daily value and the total in the beggining to reset when running again
    total = 0.0

    print(f"\nDay\tPay")
    print(f"\n===============")

    for i in range(daysWork):
        print(f"\n{i+1}\t${dailySalary:,.2f}")

        total = total + dailySalary #The total receives the daily and accumulates

        dailySalary = dailySalary * 2

    print(f"\nThe amount earn for this {daysWork} days is ${total:,.2f}")
    again = input(f"\nDo you whant to run again? Y/n ") #Enter a value for "again" before the loop tests it