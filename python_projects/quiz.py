'''
The logic of Quiz Game with Python
The Quiz game asks the player questions about animals. They have three chances to answer each question.
Each correct answer will score a point. At the end of the game, the program will reveal the player’s final score.
'''
#create a function to get the score
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    #condition set for 3 attempts
    while still_guessing and attempt < 3:
        # if the guess is right
        if guess == answer:
            print('Correct answer')
            score += 1
            still_guessing = False
        # when the guess is wrong, try to guess again
        else:
            if attempt < 2:
                guess = input('Sorry Worng guess, guess again...')
            attempt += 1
    # attempt reached to 3 , show the correct answer      
    if attempt == 3:
        print('Correct answer is', answer)
        
score = 0

print("Guess the Animal")

guess1 = input("Which bear lives at the North Pole? ").capitalize()
check_guess(guess1, "polar bear")

guess2 = input("Which is the fastest land animal? ").capitalize()
check_guess(guess2, "Cheetah")

guess3 = input("Which is the larget animal? ").capitalize()
check_guess(guess3, "Blue Whale")

#display the score
print("Your Score is "+ str(score))
            
    