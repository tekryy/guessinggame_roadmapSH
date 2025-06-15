import random
def get_input_in_range(minvalue, maxvalue):
    """
    Returns an input value if it is between minvalue and maxvalue
    and asks the user to enter a new value in case of a ValueError
    or the input not being between minvalue and maxvalue.
    """

    while True:
        try:
            user_input = int(input("Please enter a number between {} and {}:".format(minvalue, maxvalue)))
            if user_input >= minvalue or user_input <= maxvalue:
                return user_input
            else:
                print("Number must be between {} and {}".format(minvalue, maxvalue))
                # noinspection PyInconsistentReturns
                continue
        except ValueError:
            print("Invalid input")
            # noinspection PyInconsistentReturns
            continue

def get_difficulty(first_level, last_level):
    """
    Returns an input value serving as a selected difficulty if it is between first_level and last_level
    and asks the user to enter a new value in case of a ValueError
    or the input not being between first_level and last_level.
    """

    while True:
        try:
            difficulty_range = range(int(first_level), int(last_level) + 1)
            chosen = int(input("Enter a difficulty level between {} and {}:".format(first_level, last_level)))
            if chosen in difficulty_range:
                return chosen
            else:
                print("Difficulty is out of range")
                # noinspection PyInconsistentReturns
                continue
        except ValueError:
            print("Please enter a valid integer.")
            # noinspection PyInconsistentReturns
            continue



print("Welcome to my guessing game!")
number = random.randint(0, 101) # The number which the user has to guess
tries_per_level = [10,5,3] # defines the number of tries the user gets per difficulty level
selected_difficulty = get_difficulty(1,3) # selects difficulty with help of function
tries = tries_per_level[selected_difficulty - 1] # selects tries based on selected difficulty
print("You get {} guesses!".format(tries))
guessed_correctly = False
while tries > 0:
    guess = get_input_in_range(1, 100)
    if guess == number:
        tries -= 1
        guessed_correctly = True
        break
    else:
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        tries -= 1
        if tries > 0:
            print("Guess again, you have {} tries left".format(tries))
if not guessed_correctly:
    print("No tries left.")
elif guessed_correctly:
    print("You got it! The number was {}!".format(number))
    if tries_per_level[selected_difficulty - 1] - tries == 1:
        print("It took you 1 guess! That's really lucky!")
    else:
        print("It took you {} guesses!".format(tries_per_level[selected_difficulty - 1] - tries))

