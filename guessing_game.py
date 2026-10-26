import random
print("============")
print("GUESSING NUMBER GAME")

print("I will select a number between 1 and 100.")
print("Try guessing the number")

secret_number= random.randint(1, 100)

print("\nChoose your level:")
print("Easy- 10 attempts")
print("Medium- 7 attempts")
print("Hard- 5 attempts")

Level = input("Enter Easy, Medium, or Hard:").strip().lower()

while Level not in ["easy", "medium", "hard"]:
    print("Invalid entry. Please choose Easy, Medium or Hard.")
    Level= input ("Enter your Level:").strip ().lower()

attempt_limits = { "easy": 10, "medium": 7, "hard": 5 }

max_attempts = attempt_limits [Level]
attempts_used = 0
guessed_correctly = False

print(f"\nYou have selected {Level.title()} mode.")
print (f"you have {max_attempts} attempts to guess the number.")

while attempts_used <max_attempts and not guessed_correctly:
     
    try:       
        guess= int(input("\nEnter your guess (1-100):"))
        if guess <1 or guess > 100:
            print ("please enter number between 1 and 100.")
    except ValueError:
            print("Invalid entry. Please try again.")
            continue

    attempts_used += 1
    remaining_guesses = max_attempts - attempts_used

    if guess == secret_number:
            guessed_correctly = True
            print("\n Correct!")
            print(f"The secret number was {secret_number}.")
            print(f"you guessed it in {attempts_used} attempt.")
            print (f"Remaining guesses: {remaining_guesses}")

    elif guess > secret_number:
            print("Yooh, too high!")
            print(f"Remaining guesses: {remaining_guesses}")

    else:
            print ("Well, too low!")
            print (f"Remaining guesses: {remaining_guesses}")

if not guessed_correctly:
    print("\nGame Over! You have run out of attempts.")
    print(f"The correct number was {secret_number}")


print("\n The End!")







