# The Hangman Game
# - The program randomly selects a word from a list of secret words.
# - The player has limited chances to guess the word.
# - When a correct letter is guessed, it is revealed in its correct position.
# - The player wins if all letters are guessed before running out of chances.
# - For simplicity, the program gives word length + 2 chances.


import random
import requests


def generate_list_of_words():  # >>>>
    # NOTE: This may become unreliable with network issues or if website is down
    # Consider random_word library (real words, not scrambled strings)
    words_wiki = "https://www.mit.edu/~ecprice/wordlist.10000"
    __r = requests.get(words_wiki)
    text_content = __r.content.decode("utf-8")  # decode raw bytes from requests
    list_of_words = text_content.splitlines()
    return list_of_words
# <<<<

def get_random_word(list_of_words):  # >>>>
    random_word = random.choice(list_of_words)
    return random_word
# <<<<

def obfuscate_word(rand_word):  # >>>>
    obfuscated_word = ["_"] * len(rand_word)
    return obfuscated_word
# <<<<

def guess_random_word(rand_word, obfuscated_word):  # >>>>
    attempt = 0
    max_attempts = len(rand_word) + 2
    guessed_chars = set()
    print(f"WORD TO GUESS: [{'_,'.join(obfuscated_word)}]")
    while attempt < max_attempts:
        number_of_guessed_chars = 0
        inp = input("Enter a character: ").lower()
        # make sure user inputs only one character
        if len(inp) != 1 or not inp.isalpha():
            print("INFO: Please enter only one letter character!")
            continue
        # check for already guessed characters
        if inp in guessed_chars:
            print(f"INFO: The character [{inp}] has already been used. Try again.")
            continue # don't increase guess counter
        guessed_chars.add(inp)
        attempt += 1
        # update obfuscated_word
        for i, c in enumerate(rand_word):
            if c == inp:
                obfuscated_word[i] = inp
                number_of_guessed_chars += 1
        # check for victory condition
        win_game = True
        for c in rand_word:
            if c != ' ' and c not in obfuscated_word:
                win_game = False
                break
        if win_game:
            print(f"WORD TO GUESS: [{'_,'.join(obfuscated_word)}]")
            print("SUCCESS! You guessed the word!")
            return
        print(f"INFO: Attempt: {attempt}. Attempts left: {max_attempts - attempt}")
        print(f"CURRENT WORD: [{','.join(obfuscated_word)}]")
        print("---------------------------------------------------------------------")
    print(f"FAILURE! Better luck next time!")
    print(f"ORIGINAL WORD: [{','.join(rand_word)}]")
    return
# <<<<

def greet_user():  # >>>>
    print("---------------------------------------------------------------------")
    username = input("Who are you? ")
    print("Hello", username, "!")
    print("Objective:\t Guess the word.")
    print("Gameplay:\t Guess characters.")
    print("Rules:\t\t You may guess (word length + 2) times.")
    print("\t\t Guessed character is revealed.")
    print("---------------------------------------------------------------------")
# <<<<

def main():  # >>>>
    # Hello
    greet_user()
    # Generate the data
    m_word_list = generate_list_of_words()
    m_random_word = get_random_word(m_word_list)
    m_obf_word = obfuscate_word(m_random_word)
    # Use the data
    guess_random_word(m_random_word, m_obf_word)


if __name__ == "__main__":
    main()
# <<<<

# vim: fmr=>>>>,<<<< fdm=marker
