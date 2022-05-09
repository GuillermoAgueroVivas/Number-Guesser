import random
import time

print("Walcome to the Random Number Guesser. I am going to pick a random number between 1 and 100 and your job is to figure out what number that is ;)\n")
# With this line I am able to make the program wait 3 seconds before it runs the next line
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("Please enter your guess from 1 to 100: "))
correct_number = random.randint(1, 100)
guess_count = 1

while guess != correct_number:
    if guess > 100:
        guess = int(input(
            "\nYour guess was higher than 100!\nPlease enter your guess from 1 to 100: "))
    elif guess > correct_number:
        guess = int(input(
            "\nYour guess was higher than the correct answer \nPlease enter your guess from 1 to 100: "))
    else:
        guess = int(input(
            "\nYour guess was lower than the correct answer.\nPlease enter your guess from 1 to 100: "))
    guess_count += 1

print(
    f"\nCongratulations, you got the correct answer which was the number {correct_number}!")

if guess_count == 1:
    print(f"It took you {guess_count} try to figure it out :)")
else:
    print(f"It took you {guess_count} tries to figure it out :)")

time.sleep(7)
