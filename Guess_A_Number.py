import random


# Function for generating a random number between 1 and 100
def guess_a_number():
    random_number = random.randint(1, 100)

    print("Welcome to Guess A Number!")
    print("I have selected a random number between 1 and 100. Try to guess it.")

    attempts = 0
    
    # Getting user input for a guess
    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        # Checking if the guess is correct
        if user_guess == random_number:     
            print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
            break
        elif user_guess < random_number:
            print("Try again. The number is greater.")
        else:
            print("Try again. The number is smaller.")


if __name__ == "__main__":
    guess_a_number()
    