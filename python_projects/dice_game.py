# import libraries
import random

#options for the computer 
choices = ['Rock', 'Paper', 'Scissor']
computer = random.choice(choices)

player = False
cpu_score = 0
player_score = 0

#take the input and loop through the choices
while True:
    #take a input and capitalize it
    player = input('Enter Rock/Paper/Scissor/End: ').capitalize()
    
    #if player is = to computer then its a tie
    if player == computer:
        print('Tie')
        
    # if player is rock and computer is paper then player looses
    # else player is rock and computer is scissor then computer looses
    elif player == 'Rock':
        if computer == 'Paper':
            print(f'You loose, {computer} covers {player}')
            cpu_score += 1
        else:
            print(f'you win!, {player} smash {computer}')
            player_score += 1
    
    # if player is paper and computer is scissor then player looses
    # else if player is paper and computer is rock and computer looses
    elif player == 'Paper':
        if computer == 'Scissor':
            print(f'You loose, {computer} cut {player}')
            cpu_score += 1
        else:
            print(f'you win!, {player} cover {computer}')
            player_score += 1
    
    # if player is scissor and computer is rock then player looses
    # else if player is scissor and computer is paper then computer looses
    elif player == 'Scissor':
        if computer == 'Rock':
            print(f'You loose, {computer} break {player}')
            cpu_score += 1
        else:
            print(f'you win!, {player} cut {computer}')
            player_score += 1
    
    #to end the game
    elif player == 'End':
        print(f'Final score:\n')
        print(f'cpu score: {cpu_score}\n')
        print(f'player score: {player_score}\n')
    
    break