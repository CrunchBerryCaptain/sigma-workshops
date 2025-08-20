import random


def play_game():
    """Starts the R-P-S game"""

    user = get_user_choice()
    cpu = get_cpu_choice()
    winner = decide_winner(user, cpu)
    message = f"\nYour move: {user}\nCPU's move: {cpu}\n\n{winner}\n"

    return message


def get_user_choice() -> str:
    """Gets the user's move"""

    choice = int(input("""Pick a number:
                   1. Rock
                   2. Paper
                   3. Scissors\n"""))

    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"
    else:
        return "Error"


def get_cpu_choice() -> str:
    """Randomly selects a CPU move"""

    choice = random.choice(["Rock", "Paper", "Scissors"])
    return choice


def decide_winner(user: str, cpu: str) -> str:
    """Decides who wins the game"""

    if user == cpu:
        return "It's a draw :O"
    elif (
        (user == "Rock" and cpu == "Scissors") or
        (user == "Paper" and cpu == "Rock") or
        (user == "Scissors" and cpu == "Paper")
    ):
        return "You win :)"
    else:
        return "You lost :/"


print(play_game())
