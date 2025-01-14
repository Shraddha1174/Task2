import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")
    
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))  # Take user's guess
            attempts += 1

            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    guess_the_number()
  
