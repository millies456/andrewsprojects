import random
#myles Jeune
#https://www.geeksforgeeks.org/random-numbers-in-python/
#citation used in previous classes, just a library import.
round = 0
guess = 0
beginning = int(input("choose a start for a range for the whole game:   "))
end = int(input("choose a end for a range for the whole game no changes:  "))
while(beginning == end):
    print("really dont be a cheater")
    beginning = int(input("choose a start for a range for the whole game:   "))
    end = int(input("choose a end for a range for the whole game no changes:  "))
#make the user make a beginning and end range
#was going to implement an if statement so the end value is less than the beginning value but random import already declares that
while(True):
    mystery = random.randint(beginning, end) 
   
    #didnt  know if i should make the user constantly make new and old ranges just make the user keep the same range 

    # will make the user  guess the number
  
    # get user input
    guess = input("my guess is :   ")
    try:
        # try and see if user does not give int
        guess = int(guess)
        if(guess == mystery):# if the guess in within range, end the loop
            print("correct answer")
            guess = input("would you like to continue:   ")
        else:
                print("wrong answer")
                #each time the user
                print("random number is")
                print(mystery)
                print("Round")
                round = 0
                print(round)
                break
            #the user is given a decision to end the game if he or she wins, the game automatically breaks when the user gets an answer wrong
        if(guess == "no"):
            break
        if(guess == "yes"): 
           True
           #if the user is correct he will be asked to move on if he says yes then the round will be added by 1
           round = round + 1
           print("round- ")
           print(round)
    except:
        print("only integers")
    
