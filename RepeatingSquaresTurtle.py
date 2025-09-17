#Joao L Classio 09/16/2025 RepeatingSquares.py(PE4.3)

#This turtle program will draw a sequence of squares. You'll be asked for the length 
#of the first square, the increment for the subsequent squares and the number of squares.

#Inporting the turtle and set where it should start
import turtle
turtle.speed(5)
turtle.hideturtle()
turtle.penup()
turtle.goto(300,-300)
turtle.pendown()
turtle.setheading(90)

#Declaring and initializing variables
firstLength = 0
incrementLenght = 0
numberOfSquares = 0
again = "y"

#Drawing processing
while again.lower() == "y": #Keeps the program runing until told to stop
    firstLength = turtle.numinput("Length","Enter a integer length for the first square:",5)
    incrementLength = turtle.numinput("Increment","Enter a integer increment for next square:",5)
    numberOfSquares = int(turtle.numinput("Squares","Enter how many squares for the drawing:",1))
    
    for i in range(numberOfSquares): #Repets the "square drawing" until reach the number of squares asked
        for j in range(4): #Draws the square
            turtle.forward(firstLength)
            turtle.left(90)    
        firstLength += incrementLength #Increments the increment to the last square length after completing the square 
        
    again = turtle.textinput("Run Again?","Do you whant to run it again? Y/n")
    turtle.clear() #Clears the screen    
    
turtle.bye()    
