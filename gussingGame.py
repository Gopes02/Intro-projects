# The following program randomly picks a number between a chosen set of numbers and the user has to guess what is the number it has picked  


import random 
import math

# Adjustables 
x = 1                           # Lowest number for randomizer
y = 20                          # Highest number for randomizer
mA = 10                         # Max attempt for user 

# The adjusted 
number = random.randint(x,y)    # Randomly picks an int; adjusted based on x and y; uses the random library 
maxAttempt = int (mA)           # Max attempt for user; adjusted based on mA

userAttempt = int (1)           # Attempts by user counter

# Welcome message along with User input of name, prints name and number of attempts, range of number to pick from   
userName = input("\nWelcome to the guessing game!! \nWhat is your name: ")                                                      # User input of their name 
print("\n")
print(userName,"you will have",maxAttempt,"attempts to guess the correct number." )                                             # prints name and number of attempts

print("\nPick a whole number between",x,"and",y)                                                                                  
print("If a whole number is not enetered, your value will changed by the 'floor' or 'ceil' functions.")                          
print("If decimal value of your picked number is less than .5 => 'floor' function otherwise 'ceil' function\n\n")


# Loop will run till User Attempts > Attempts allowed or the correct number was picked
while (userAttempt <= maxAttempt):              
    uG = input("\nWhat is your guess?: ")                   # User guess
    uG_float = float(uG)                                    # changes to float to use floor and ceiling functions 
    
    if(uG_float - math.floor(uG_float) < .5 ):              # floor function to convert to int for any decimal value less than .5
        floor = math.floor(uG_float)
        userGuess = int (floor)                             # Converts user guess from string to int 
    else:
        ceiling = math.ceil(uG_float)                       # ceiling function to convert to int for any decimal value more than .5
        userGuess = int (ceiling)                           # Converts user guess from string to int 
    print("The number you picked is:",userGuess)
    
    if (userGuess >= x and userGuess <= y):
        
        if (userGuess < number):                                                                        # If user guess is lower than the correct number, prints low
            print("your guess is low")
            userAttempt = userAttempt + 1                                                               # Increments by one if the guess was not correct 
        elif (userGuess > number):                                                                      # Doesn't meet the first if statement so it checks this statement  
            print("your guess is High")                                                                 # If user guess is higher han the correct number, prints high
            userAttempt = userAttempt + 1                                                               # Increments by one if the guess was not correct 
        elif(userGuess == number):                                                                      # If other two statements are not met then checks this statement. Could of just used a else statement as well. checks if guess was correct 
            print("Congrats, you have guessed the correct number in", userAttempt, "attempts")
            break                                                                                       # IF this statement is met, it ends the loop because no more guesses are needed 
    else:
        print("Please pick a whole number between",x,"and",y)      
    
if(userGuess != number):                                                                                # If all attempts are used and the correct number was not picked, we are printed the correct answer 
        print("You have not guessed the correct number in", maxAttempt, "attempts. The number was",number)
    
