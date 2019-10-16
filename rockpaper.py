"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of
congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""

import random
print('Rock, Paper, Scissors - Presented by Andrew M McCall')
print("\n\tEnter rock, paper, or scissors and see if you can beat the computer!")

moves = ['rock', 'paper', 'scissor']

round = True

while round:
    move = input('\nenter your move: ')
    if move.lower() not in moves:
        print('Invalid Entry!')
        continue
    else:
        computer_move = random.choice(moves)

    print("\nThe computer played: " + str(computer_move))

    if move == 'rock' and computer_move == 'rock':
        print('go again!')
        round
    elif move == 'rock' and computer_move == 'scissor':
        print('you win')
        again = input("Go Again? (y/n): ")
        if again == 'n':
            break
        else:
            round
    elif move == 'rock' and computer_move == 'paper':
        print('you lose')
        again = input("Go Again? (y/n): ")
        if again == 'n':
            break
        else:
            round
    elif move == 'paper' and computer_move == 'paper':
        print('go again!')
        round
    elif move == 'paper' and computer_move == 'rock':
        print('You Win!')
        again = input("Go Again? (y/n): ")
        if again == 'n':
            break
        else:
            round
    elif move == 'paper' and computer_move == 'scissor':
        print('You Lose!')
        again = input("Go Again? (y/n): ")
        if again == 'n':
            break
        else:
            round
    elif move == 'scissor' and computer_move == 'scissor':
        print('Go Again!')
        round
    elif move == 'scissor' and computer_move == 'rock':
        print('You Lose!')
        again = input("Go Again? (y/n): ")
        if again == 'n':
            break
        else:
            round
    else:
        if move == 'scissor' and computer_move == 'paper':
            print('You Win!')
            again = input("Go Again? (y/n): ")
            if again == 'n':
                break
            else:
                round



print('Thank you for playing!')
