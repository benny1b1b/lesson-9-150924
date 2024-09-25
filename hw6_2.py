import random

attempts= 0
number: int = random.randint(1,100)
while True:
    your_guess: int = int(input("your guess: "))
    attempts += 1
    if your_guess > number:
        print(f"too big {attempts}")
    elif your_guess < number:
        print(f"too small {attempts}")
    else:
        print(f"bingo! {attempts} attempts were made.")
        break
