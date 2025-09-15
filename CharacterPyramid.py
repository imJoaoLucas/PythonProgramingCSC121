#Joao L Classio 09/15/2025 CharacterPyramid(PE4.2)

character = input("What character do you whant to build your tree?")
rowsAndColumns = int(input("Insert the number of rows and columns?"))
characterTimes = rowsAndColumns

for j in range(rowsAndColumns):
    print(f"\n{character * characterTimes}")
    characterTimes = characterTimes - 1 