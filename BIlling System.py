import random
print("Welcome to Number Guessing Game!")
while True:
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1,100)
  guess=None
  while guess!=number:
      try:
        guess=int(input("Enter your guess: "))
        if guess>number:
          print("Oh! No Your guess is too high.Try again")
        elif guess<number:
          print("Oh! No Your guess is too low.Try again")
        else:  
          print(f"Congratulations! You guessed the number correctly.")
      except ValueError:
        print("Invalid input. Please enter a valid number.")
  while True:
    playagain=input("If you want to play again enter 'y' or 'n' to exit: ")
    if playagain=='y':
      break
    elif playagain=='n':
      print("Thanks for playing!")
      break
    else:
      print("Invalid input. Please enter 'y' or 'n'.")
      continue

      