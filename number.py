import random

def get_random_number():
    return random.randint(1, 100)

Tries = 0

randomnumber = get_random_number()
print(randomnumber)
while True:
    randominput = int(input("Guess the number between 1 and 100: "))
    if randominput == randomnumber:
        print("You guessed correctly! Tries: ", Tries)
        break
    else:
        print("Try again!")
        Tries += 1
