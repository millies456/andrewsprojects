import random
# Sam Schaeffler
# CINF 108

# print program description
print("This program allows you to guess a random number")
random = random.randint(1, 2) # generate random number between 1 and 10
print("(pssstt, the random number is", ranNum, ")")
# set incorrect to True so the while loop will start, later it will end when given a proper guess
incorrect = True
# guess initialized to 0 to make sure there are no issues
guess = 0

# while loop runs as long as there is no correct answer
while(incorrect):
    # get user input
    guess = input("Please input a number between 1-2: ")
    try:
        # try and see if user does not give int
        guess = int(guess)
    except:
        # if an integer was not given, return this message
        print("Please only input numbers.")
    else:
        # if an integer was given, make sure the guess is changed to type int
        guess = int(guess)
        # check to see if the guess is within the range
        if(guess >= 1) and (guess <= 10):
            # if the guess in within range, end the loop
            incorrect = False
        else:
            # if the guess is not within the range, do not end loop and give error message
            print("Please return a number in the correct range.")
# check to see if guess is correct
if(guess == random):
    # return correct message
    print("You've guessed the number! The random number is", random)
else:
    # if incorrect, return failure message
    print("You failed to guess the number. The correct answer was", random)