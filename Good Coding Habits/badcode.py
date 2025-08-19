import random


def check(str, guess):
    result = ['_' for _ in range(len(str))]
    for i, x in enumerate(guess):
        if x == str[i]:
            result[i] = x
        elif letter in str:
            result[i] = '?'
    return result


def gen_wor(wlist):
    return random.choice(wlist)


def func():
    i = gen_wor()
    go = 5
    while go > 0:
        input1 = input("Enter your guess: ")
        if len(i) != 5:
            print("Please enter a 5-letter word.")
            continue
        result = check(i, input1)
        print(' '.join(result))
        if input1 == i:
            print("Congratulations! You've guessed the word.")
            return
        go -= 1
    print(f"Sorry, you didn't guess the word. The word was {i}.")


list2 = ["apple", "place", "grape", "chair", "spear", "green",
         "plant", "house", "water", "money", "tiger", "panda"]
func(list2)
