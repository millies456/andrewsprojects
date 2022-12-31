import random

round = 0
beginning = int(input("choose a start for a range for the whole game: "))
end = int(input("choose a end for a range for the whole game no changes: "))
while(True):
    ranNum = random.randint(beginning, end) 
    # generate random number between 1 and 10
    print("random number is")
    print(ranNum)
    guess = 0
    # get user input
    guess = input("the range is from")
    try:
        # try and see if user does not give int
        guess = int(guess)
        guess = int(guess)
        if(guess == ranNum):# if the guess in within range, end the loop
            print("correct answer")
            guess = input("would you like to continue")
        else:
                print("wrong answer")
                print("answer is")
                print(ranNum)
                print("Round")
                round = 0
                print(round)
                break
        if(guess == "no"):
            break
        if(guess == "yes"): 
           True
           round = round + 1
           print("round- ")
           print(round)
    except:
        print("Please only input numbers.")
    
        
            


 

