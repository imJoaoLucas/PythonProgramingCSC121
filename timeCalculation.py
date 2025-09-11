#Joao L. Classio 09/10/2025 timeCalculation.py(PE3.2)
#This program calculates a formated time after receiveing a number of seconds.

#Declaring and initializing variables and constants
SECONDS_MINUTES = 60
SECONDS_HOUR = 3600
SECONDS_DAY = 86400

secondsEntry = int(input("Enter the number of seconds to format:"))
secondsUsed = 0
secondsLeftover = 0
result = 0

#Calculation

print("The %d second(s) you entered is equal to: " % secondsEntry)
daysEntry = secondsEntry // SECONDS_DAY #Calculates how many days without considering "partial days"
secondsUsed = daysEntry * SECONDS_DAY #Calculates how many seconds have already been displayed as "days"
secondsLeftover = secondsEntry - secondsUsed #The amount of seconds left for next steps

#Calculation for hours - it uses the same method as days
hoursEntry = secondsLeftover // SECONDS_HOUR
secondsUsed = hoursEntry * SECONDS_HOUR
secondsLeftover -= secondsUsed

#Calculation for minutes - it uses the same method as days
minutesEntry = secondsLeftover // SECONDS_MINUTES
secondsUsed = minutesEntry * SECONDS_MINUTES
secondsLeftover -= secondsUsed

#Result display
if daysEntry > 0: #Only print "day(s)" when there is at least 1 day
    print(f"%d day(s)"% daysEntry)
if hoursEntry > 0: #Only print "hour(s)" when there is at least 1 hour
    print(f"%d hour(s)"% hoursEntry)
if minutesEntry > 0: #Only print "minute(s)" when there is at least 1 minute
    print(f"%d minute(s)" % minutesEntry)
    print(f"%d second(s)" % secondsLeftover)#If there is at least 1 minute, second(s) need to be calculated
if secondsEntry < 60:
    print(f"%d second(s)" % secondsEntry)#Only used if input is less than 60