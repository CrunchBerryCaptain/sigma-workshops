import random


def check(word: str, guess: str) -> str:
    result = ['_' for char in range(len(word))]
    for idx, char in enumerate(guess):
        if char == word[idx]:
            result[idx] = char
        elif char in word:
            result[idx] = '?'
    return result


def generate_random_word(word_list: list) -> str:
    return random.choice(word_list)


def start_game():
    word = generate_random_word(random_word_list)
    attempts = 5

    while attempts > 0:
        guess = input("Enter your guess: ")

        if len(word) != 5:
            print("Please enter a 5-letter word.")
            continue

        result = check(word, guess)
        print(' '.join(result))

        if guess == word:
            print("Congratulations! You've guessed the word.")
            return

        attempts -= 1

    print(f"Sorry, you didn't guess the word. The word was {word}.")


random_word_list = ["apple", "place", "grape", "chair", "spear", "green",
                    "plant", "house", "water", "money", "tiger", "panda"]

start_game()
