import random

correct = 'you guessed correctly!'
Too_Low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    while True:
        try:
            low = int(input("Enter the minimum number to guess\n"))
            high = int(input("Enter the maximum number to guess\n"))
            if high <= low:
                high = int(input("Enter a higher number\n"))
            return low, high
        except ValueError:
            print("Numbers only please and thankyou")



def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess(guessCount):
    '''get user's guess'''
    guessCount+= 1
    return int(input('Guess the secret number? ')), guessCount


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return Too_Low
    if guess > secret:
        return too_high

def playAgain():
    userInput = input('Enter Y to play again, N to close:\n')
    if userInput != 'Y' or userInput != 'N':
        userInput = input('Please Enter Y or N\n')
    if userInput == 'Y':
        return True
    elif userInput == 'N':
        return False



def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    guessCount = 0

    while True:

        try:

            guess, guessCount = get_guess(guessCount)

            if guess <= 0 or guess > 10:
                print('Enter 1 - 10')
                guess = int(input('Guess the secret number? '))

            result = check_guess(guess, secret)
            print(result)

            if result == correct:
                print("It took {} guesses".format(guessCount))
                if playAgain():
                    guessCount = 0
                    secret = generate_secret(low, high)
                else:
                    break

        except ValueError:
            print('Error, only enter numbers')




if __name__ == '__main__':
    main()
