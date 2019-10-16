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

wins = 0
losses = 0
human_moves = []
computer_moves =[]
round = True

while round:
    move = input('\nenter your move: ')
    human_moves.append(move.lower())
    if move.lower() not in moves:
        print('Invalid Entry!')
        continue
    else:
        computer_move = random.choice(moves)
        computer_moves.append(computer_move)

    print("\nThe computer played: " + str(computer_move))

    if move == 'rock' and computer_move == 'rock':
        print('go again!')
        round
    elif move == 'rock' and computer_move == 'scissor':
        print('you win')
        wins += 1
        again = input("Go Again? (y/n): ")
        if again == 'n':
            break
        else:
            round
    elif move == 'rock' and computer_move == 'paper':
        print('you lose')
        losses += 1
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
        wins += 1
        again = input("Go Again? (y/n): ")
        if again == 'n':
            break
        else:
            round
    elif move == 'paper' and computer_move == 'scissor':
        print('You Lose!')
        losses += 1
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
        losses += 1
        again = input("Go Again? (y/n): ")
        if again == 'n':
            break
        else:
            round
    else:
        if move == 'scissor' and computer_move == 'paper':
            print('You Win!')
            wins += 1
            again = input("Go Again? (y/n): ")
            if again == 'n':
                break
            else:
                round


total_rounds = wins + losses
print('Thank you for playing!')
print("\nYou Won: " +str(wins) + " times.")
print("\nYou Lost: " + str(losses) + " times.")
print("\nYou played: " + str(total_rounds) + " rounds.")
print("\nYou played Rock: " + str(human_moves.count('rock')) + " times.")
print("\nYou played Paper: " + str(human_moves.count('paper')) + " times.")
print("\nYou played Scissor: " + str(human_moves.count('scissor')) + " times.")
print("\nYou made a total of: " + str(len(human_moves)) + " moves.")

# computer results
print("\nBot played Rock: " + str(computer_moves.count('rock')) + " times.")
print("\nBot played Paper: " + str(computer_moves.count('paper')) + " times.")
print("\nBot played Scissor: " + str(computer_moves.count('scissor')) + " times.")
print("\nBot made a total of: " + str(len(computer_moves)) + " moves.")
