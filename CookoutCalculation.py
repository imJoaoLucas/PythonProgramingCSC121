#Joao L. Classio 9/10/2025 CookoutCalculation.py(PE3.1)
"""This program receives the the number of guests to a cookout and how many
hot dogs each people will eat, and return the minumum number of hot
dog and hot dog buns packages, and the number of left overs for both."""

#Declaring and initializing constants
WIENER_PACK = 10
HOT_DOG_BUN_PACK = 8

#Declaring and initializing variables 
peopleInvited = int(input("Enter the number of people attending the cookout: "))
hotDogPerPeople = int(input("Enter the number of hot dog for each person: "))

hotDogTotal = peopleInvited * hotDogPerPeople
bunPackRequired = 1 #Both initialized as "1" as this is the lowest required
wienerPackRequired = 1 #considering that the user can't enter an invalid value

#Calculation

moduloDogToWiener = hotDogTotal % WIENER_PACK
moduloDogToBun = hotDogTotal % HOT_DOG_BUN_PACK

#Requirement calculation
if hotDogTotal >= HOT_DOG_BUN_PACK: #If is it required more than one bun package
    if moduloDogToBun != 0:
        bunPackRequired = (hotDogTotal // HOT_DOG_BUN_PACK) + 1
    else:
        bunPackRequired = hotDogTotal / HOT_DOG_BUN_PACK

if hotDogTotal >= WIENER_PACK: #If is it required more than one hot dog package
    if moduloDogToWiener != 0:
        wienerPackRequired = (hotDogTotal // WIENER_PACK) + 1
    else:
        wienerPackRequired = hotDogTotal / WIENER_PACK

#Left overs calculation
bunLeft = (bunPackRequired * HOT_DOG_BUN_PACK) - hotDogTotal
wienerLeft = (wienerPackRequired * WIENER_PACK) - hotDogTotal

#Results display
print(f"Minimum hot dogs and buns needed:", hotDogTotal)
print(f"\nMinimum packages of hot dogs needed:", wienerPackRequired)
print(f"Minimum packages of hot dog buns needed:", bunPackRequired)
print(f"\nHot dogs left over:", wienerLeft)
print(f"Hot dog buns left over:",bunLeft)
