import random
upper_range=100
lower_range=1
no_guess=random.randint(lower_range,upper_range)
attempt=0
print("Welcome to number guessing game")
print(f"Your no is between {lower_range} and {upper_range}")
while True:
    guess=int(input("Enter your guess"))
    if no_guess==guess:
        print("Congrats You gueesed the number ")
        break
    elif guess>no_guess:
        print("Your guess is high")
    else:
        print("Your guess is low")
    attempt+=1
print(f"You took {attempt} attempts")
print("Thank You for playing")



