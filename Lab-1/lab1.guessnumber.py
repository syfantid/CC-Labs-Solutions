import random

# Allows multiple games
while(True):
    random_number = random.randint(1, 206)
    number_guess=0

    #Allows 5 guesses only
    while(number_guess<5):
        #Typed character must be number
        try:
            guess = int(input('Guess the number between 1 and 20: '))
        except ValueError :
            print("Plese give a number!")
            continue

        #Typed number must be in the range of 1 and 20
        if(guess > 20 or guess < 1):
            print("Plese give a number in the range of 1 and 20")
            continue
        number_guess += 1
        if(guess == random_number):
            print('Excellent guess! You succeeded in your '+ str(number_guess) + " try")
            break
        elif(guess > random_number):
            print('Sorry, number is too high. Try again!')
        else:
            print('Sorry, number is too low. Try again!')
    if(number_guess==5):
        print('Sorry you are out of tries :(')

    # Allow user to play again
    play_again = input('Do you want to play again (y/n): ')
    if(play_again == 'n' or play_again != 'y'):
        print('Goodbye! Thank you for playing with us!')
        break
