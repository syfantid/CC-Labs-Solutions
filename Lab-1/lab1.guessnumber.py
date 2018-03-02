import random

# Allows multiple games
while(True):
    random_number = random.randint(1, 20)

    # Allows multiple guesses15
    while(True):
        guess = int(input('Guess the number between 1 and 20: '))
        if(guess == random_number):
            print('Excellent guess!')
            break
        elif(guess > random_number):
            print('Sorry, number too high. Try again!')
        else:
            print('Sorry, number too low. Try again!')

    # Allow user to play again
    play_again = input('Do you want to play again (y/n): ')
    if(play_again == 'n' or play_again != 'y'):
        print('Goodbye! Thank you for playing with us!')
        break




