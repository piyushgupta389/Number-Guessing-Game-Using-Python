import random

def get_difficulty():
    print("\n1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    while True:
        choice = input("Choose difficulty (1/2/3): ")
        if choice == "1":
            return 1, 50, 10
        elif choice == "2":
            return 1, 100, 7
        elif choice == "3":
            return 1, 200, 5
        else:
            print("Invalid choice!")

def play_game():
    low, high, max_attempts = get_difficulty()
    secret = random.randint(low, high)
    attempts = 0
    guesses = []

    print(f"\nGuess the number between {low} and {high}")
    print("Type 'quit' to exit.\n")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts+1}/{max_attempts}: ")

        if guess.lower() == "quit":
            print(f"Game exited. Number was {secret}")
            return False

        if not guess.isdigit():
            print("Enter valid number!")
            continue

        guess = int(guess)

        if guess < low or guess > high:
            print(f"Enter between {low} and {high}")
            continue

        attempts += 1
        guesses.append(guess)

        if guess == secret:
            print(f"\nCorrect! You guessed in {attempts} attempts.")
            print("Your guesses:", guesses)
            return True

        elif abs(secret - guess) <= 5:
            print("Very Close!")
        elif guess < secret:
            print("Too Low!")
        else:
            print("Too High!")

        print("Attempts left:", max_attempts - attempts)

    print(f"\nGame Over! Number was {secret}")
    print("Your guesses:", guesses)
    return False


print("===== NUMBER GUESSING GAME =====")

total_wins = 0

while True:
    if play_game():
        total_wins += 1

    print("Total wins this session:", total_wins)

    again = input("\nPlay again? (yes/no): ")
    if again.lower() not in ["yes", "y"]:
        print("Thanks for playing!")
        break
