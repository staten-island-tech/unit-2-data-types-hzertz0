import random

def get_random_number():
    return random.randint(1, 100)

Tries = 0

randomnumber = get_random_number()

# Start the guessing loop
while True:
    randominput = int(input("Guess the number between 1 and 100: "))
    Tries += 1

    if randominput < randomnumber:
        print("The number is higher!")

    elif randominput > randomnumber:
        print("The number is lower!")

    elif randominput == randomnumber:
        print("You guessed correctly! Tries:", Tries)
        break
