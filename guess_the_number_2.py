from random import randint

def choices():
    """
    acquire decision from user and check if it is correct
    :rtype: str
    :return: string from available decisions, chosen by user
    """

    available_decisions = ["too small", "too big", "you win"]
    while True:
        user_choice = input().lower()
        if user_choice in available_decisions:
            break
        else:
            print("Incorrect decision, insert too small, too big or you win")
    return user_choice


def guess_the_number():
    print("\nThink about the number between 1 and 1000 and I'll try to guess it in under 10 tries, unless you cheat!:)")
    print("\nAvailable decisions are: too small, too big, you win")
    print("Press 'Enter to start")
    input()
    min = 0
    max = 1000
    user_choice = ""
    counter = 0
    while user_choice != "you win":
        guess = int((max - min) // 2) + min
        counter += 1
        if counter > 11:
            print("Don't cheat!, ")
        print(f"Your guess is: {guess}")
        user_choice = choices()
        if user_choice == "too small":
            min = guess
        elif user_choice == "too big":
            max = guess
    print("I've guessed your number!")

if __name__ == "__main__":
    guess_the_number()
