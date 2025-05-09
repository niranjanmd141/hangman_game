import random

def choose_word():
    """Selects a random word from a list."""
    words = ["python", "java", "javascript", "kotlin", "swift", "ruby", "csharp", "go", "typescript", "php", "hangman", "challenge", "programming", "openai", "chatgpt", "artificial", "intelligence"]
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    """Displays the word with correctly guessed letters and underscores for unguessed letters."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |      
           -
        """
    ]
    return stages[6 - tries]

def hangman():
    """Plays a game of Hangman."""
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6

    print("\n🎉 Welcome to the Hangman Game! 🎉")
    print("Try to guess the word, one letter at a time. You have 6 tries!")

    while "_" in display_word(word_to_guess, guessed_letters) and incorrect_guesses < max_guesses:
        print(f"\nWord: {display_word(word_to_guess, guessed_letters)}")
        print(display_hangman(incorrect_guesses))
        guess = input("\n🔤 Guess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Invalid input. Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You've already guessed that letter. Try something new!")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("✅ Great job! You guessed a correct letter!")
        else:
            incorrect_guesses += 1
            print(f"❌ Oops! Wrong guess. You have {max_guesses - incorrect_guesses} tries left.")

    print("\n===============================")
    if "_" not in display_word(word_to_guess, guessed_letters):
        print(f"🎊 Congratulations! You guessed the word: {word_to_guess}")
    else:
        print(display_hangman(incorrect_guesses))
        print(f"💀 Game over! The word was: {word_to_guess}")
    print("===============================")

if __name__ == "__main__":
    hangman()
