import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        try:
            guess = get_guess()
            if guess <= 0 or guess > 10:
                print('Only enter 1 - 10')
                guess = get_guess()
            result = check_guess(guess, secret)
            print(result)

            if result == correct:
                break
        except ValueError:
            print('Error, only enter numbers')



if __name__ == '__main__':
    main()