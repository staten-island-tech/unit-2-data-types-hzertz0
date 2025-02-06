import random

def get_random_number():
    return random.randint(1, 100)  # Function to get a random number

# Generate the random number outside the loop, so it doesn't change after each guess
randomnumber = get_random_number()

while True:
    # Ask the user to guess the number
    randominput = int(input("Guess the number between 1 and 100: "))  # Convert input to integer
    
    # Check if the guess is correct
    if randominput == randomnumber:
        print("You guessed correctly!")
        break  # Exit the loop if the guess is correct
    else:
        print("Try again!")  # Prompt user to try again
