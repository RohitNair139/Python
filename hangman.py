import random
import nltk
# Download the words corpus if it isn't downloaded yet
nltk.download('words', quiet=True)
from nltk.corpus import words as nltk_words

# --- Prepare the Word List ---

# Get the full list of words from NLTK
words_list = nltk_words.words()

# Optional filtering: use words that are between 5 and 10 letters long
# and only alphabetic words for better game experience.
filtered_words = [word for word in words_list if word.isalpha() and 5 <= len(word) <= 10]

# Choose a random word and convert it to uppercase for consistent comparisons
word = random.choice(filtered_words).upper()

# --- Set Up Hangman ASCII Art ---
stages = [
    # 0 wrong guesses: initial empty state
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """,
    # 1 wrong guess
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,
    # 2 wrong guesses
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
       -
    """,
    # 3 wrong guesses
    """
       --------
       |      |
       |      O
       |     \\|
       |      
       |     
       -
    """,
    # 4 wrong guesses
    """
       --------
       |      |
       |      O
       |     \\|/
       |      
       |     
       -
    """,
    # 5 wrong guesses
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     
       -
    """,
    # 6 wrong guesses
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,
    # 7 wrong guesses: game over state
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """
]

# Set the number of allowed wrong guesses (lives)
lives = len(stages) - 1

# --- Initialize the Game Variables ---
display = ['_'] * len(word)  # A list of underscores for each letter in the word
guessed_letters = []  # To store guessed letters

# --- Start of the Hangman Game ---
print("Let's play Hangman!")
#print(f"(The secret word is: {word})")  # Uncomment for debugging

while lives > 0 and '_' in display:
    # Display current hangman stage, word progress, guessed letters and lives left
    print(stages[len(stages) - 1 - lives])
    print("Word: " + " ".join(display))
    print("Guessed Letters: " + ", ".join(guessed_letters))
    print(f"Lives Remaining: {lives}")
    
    # Take the player's guess
    guess = input("Guess a letter: ").upper()
    
    # Check if the user has already guessed that letter
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.\n")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        # Update the display for every occurrence of the guessed letter
        for index, letter in enumerate(word):
            if letter == guess:
                display[index] = guess
        print("Correct!\n")
    else:
        lives -= 1
        print("Wrong guess!\n")
    
    print("\n")  # Blank line for readability

# --- End of Game: Win or Lose ---
if '_' not in display:
    print("Congratulations! You guessed the word: " + word)
else:
    print(stages[len(stages) - 1])
    print("Game Over! The word was: " + word)
