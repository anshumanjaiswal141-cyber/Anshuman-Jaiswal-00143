print("================================")
print("      NUMBER GUESSING GAME      ")
print("================================")

print("Welcome to the first python project!")
print("Guess the number between 1 and 100.")

import random

# Generate random number 
secret_number = random.randint(1, 100)


# Print  gets 5 attempts
attempts = 5
used = 0

while used < attempts:
    guess = input("Enter your guess: ")


    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input! Enter a whole number.")
        continue

    if guess <1 or guess > 100: 
        print ( "Enter a number between 1 and 100.")
        continue

    used += 1 

    if guess == secret_number:
        print("Congratiulations! You guessed correctly!")
        print("Attempts used:", used)
        break

    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

        print("Attempts used:",attempts - used)

else:
    print("Game Over!")
    print("The secret number was:", secret_number)

print("Thanks for playing!")

