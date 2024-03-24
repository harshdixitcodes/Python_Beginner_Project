import random
import nltk
from nltk.corpus import words

# Ensure you've downloaded the words corpus
nltk.download('words')

# Modify the get_word function to use NLTK's words
def get_word():
    word_list = words.words()
    return random.choice(word_list).upper()

def play_hangman():
    word = get_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = [] # List to keep track of letters guessed
    tries = 6
    
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Congrats, you passed the word! you win!")
    else:
        print("Sorry, you ran out of tries. The word was "+ word +". Maybe next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                  ---
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                  ---
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                  ---
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                  ---
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                  ---
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                  ---
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                  ---
                """
    ]
    return stages[tries]

play_hangman()  