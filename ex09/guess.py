import random

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")

minimum = 1
maximum = 60

attempts = 0
guess = 0

rand = random.randint(minimum, maximum)

while guess != rand:
    print(f"What's your guess between {minimum} and {maximum}?")
    text = input(">> ")
    try:
        guess = int(text)
        attempts += 1
        if guess > rand:
            print("Too high!")
        elif guess < rand:
            print("Too low!")
    except ValueError:
        print("That's not a number.")

if rand == 42:
    print("The answer to the ultimate question of life, " +
          "the universe and everything is 42.\n" +
          "Congratulations! You got it on your first try!")
else:
    print(f"Congratulations, you've got it!\nYou won in {attempts} attempts!")
