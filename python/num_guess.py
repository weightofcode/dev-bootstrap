# ---------------------------------------------
# Guess the number between 1 and 100
# ---------------------------------------------

from random import randint

MIN_RANGE = 0
MAX_RANGE = 100


def generate_random_number():
    print("------------------------------------------")
    print(f"Generating a random number ")
    print(f"between {MIN_RANGE} and {MAX_RANGE}...")
    print("------------------------------------------")
    rn = randint(MIN_RANGE, MAX_RANGE)
    print(f"DEBUG: RNG: {rn}")
    return rn

def read_user_input():
    print("INPUT: Enter a number between 0 and 100:")
    print("------------------------------------------")
    num = int(input("Your number:",))
    return num

def main():
    rand_num = generate_random_number()
    while True:
        n = read_user_input()
        if n < rand_num:
            print(f"GUESS: Input is lower than Random Number. Please try again.")
            continue
        elif n > rand_num:
            print(f"GUESS: Input is larger than Random Number. Please try again.")
            continue
        else:
            print(f"SUCCESS: You guessed the Random Number! [{rand_num}]") 
            return

if __name__ == "__main__":
    main()
