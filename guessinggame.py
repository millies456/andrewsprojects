player1 = [1, 3, 5, 7, 9]
player2 = [1, 2, 3, 4, 5]
rounds = 0
rounds = int(rounds)

number1 = 0
number2 = 0
points = 0

print("u get 5 rounds")

for i in range(5):
    number1 = input('Player 1 type a number between 1 and 20\n')

    number1 = int(number1)

    player1[i] = number1
 
for i in range(5):

    number2 = input('Player 2 guess the number\n')

    number2 = int(number2)
    player2[i] = number2
for i in range(5):
    for x in range(5):
        if(player1[i] == player2[x]):
            points = points + 1
print("player 2 has guess player 1 ")
print(points) 
print("times")
if(points > 2):
    print("player 2 has won")
if(points < 3):
    print("player 1 has won")
print("player 1 choices ")
print(player1) 
print("player 2 guess ")
print(player2)
    
    
