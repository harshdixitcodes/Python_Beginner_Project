import random

def number_guessing_game():
    number_to_guess = random.randint(1,100)
    print(number_to_guess)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100")
    
    while True:
        attempts += 1
        try:
            player_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if player_guess < 1 or player_guess > 100:
            print("Your guess is out of bounds. Please guess a number between 1 and 100")
        else:
            difference = abs(player_guess - number_to_guess)
            if difference == 0:
                print(f"Congratulations! you have successfully guessed the number {number_to_guess},{name}")
                print(f"{name} do you wish to play more ?")
                response = input("Enter yes to play or no if you want to exit the game.")
                if (response.lower() == "yes"):
                    number_guessing_game()
                else:
                    break
            elif difference > 10:
                if player_guess < number_to_guess:
                    print("Too low. Try Again.")
                else:
                    print("Too high. Try again.")
            else:
                if player_guess < number_to_guess:
                    print("Low. Try again.")
                else:
                    print("High. Try again.")

print("Welcome to the Number Guessing Game!!!")
name = input("Before that what can I call you ?")
print(f"{name}, it's a nice name, so {name} let's get started shall we?")
number_guessing_game()
exit()