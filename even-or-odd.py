#this is a simple program that does the following
#1. ask user to enter number
#2. program will determine if value entered is even or odd

def evenOdd():
    anyNum = int(input("Please enter any real number: ")) #user input

    if anyNum%2 == 0:  #simple boolean structure with the modulos operator 
        print ("The number you entered", anyNum, "is an Even number")
    else:
         print ("The number you entered", anyNum, "is an Odd number")




evenOdd()