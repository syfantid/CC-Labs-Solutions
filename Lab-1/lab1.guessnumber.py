import random


# Checks whether a number is between a specified range
def range_check(number, lower_bound, upper_bound):
    if number > upper_bound or number < lower_bound:
        print('Plese give a number in the range of ' + str(lower_bound) + ' and ' + str(upper_bound) + '.\n')
        return False
    return True


# Game to guess a random number between a specified range
def random_number_game(lower_bound, upper_bound):
    # Allows multiple games
    while True:
        random_number = random.randint(lower_bound, upper_bound)
        number_guess = 0

        # Allows 5 guesses only
        while number_guess < 5:

            # Typed character must be number
            try:
                guess = int(input('Guess the number between ' + str(lower_bound) + ' and ' + str(upper_bound) + ': '))
            except ValueError:
                print('Plese give a number!\n')
                continue

            # Typed number must be in the range between lower bound and upper bound
            if not range_check(guess, lower_bound, upper_bound):
                continue

            # Actual game logic
            number_guess += 1
            if guess == random_number:
                print('Excellent guess! You succeeded in your ' + str(number_guess) + ' try!\n')
                break
            elif guess > random_number:
                print('Sorry, number is too high. Try again!\n')
            else:
                print('Sorry, number is too low. Try again!\n')

        if number_guess == 5:
            print('Sorry you are out of tries. :(\n')

        # Allow user to play again
        play_again = input('Do you want to play again (y/n): ')
        if play_again == 'n' or play_again != 'y':
            print('Goodbye! Thank you for playing with us!\n')
            break


def main():
    random_number_game(1, 20)


if __name__ == "__main__":
    main()
