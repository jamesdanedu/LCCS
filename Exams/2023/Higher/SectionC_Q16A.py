# Question 16(a)
# Examination Number:  <enter your exam number here!>
from random import randint

guesses = []   # part (vi)

def guess_game(max_guesses_allowed, difficulty):
  if (difficulty == 'H'):                                                    #part (v)
    secret_number = randint(1, 100)                                          #part (v)
  else:
    secret_number = randint(1, 5)
  guess_count = 0
  user_guess = 0
  while (user_guess != secret_number) and (guess_count < max_guesses_allowed):          # part (iii)  
    user_guess = int(input("Enter your guess: "))
    guess_count += 1               #Increase guess_count by 1
    if (guesses.count(user_guess) != 0):                                              #part (vi)
      print ("You already guessed this number")                                       #part (vi)
    else:                                                                             #part (vi)  
      guesses.append(user_guess)                                                      #part (vi)
    if user_guess == secret_number:
      print("Congratulations! You win!")
      print("You took ", guess_count, " guesses")                  # part (i)
    elif user_guess < secret_number:                               # part (ii)
      print ("Sorry! Your guess was too low")                      # part (ii) 
    elif user_guess > secret_number:                               # part (ii)
      print ("Sorry! Your guess was too high")                     # part (ii)

print("Welcome to the guessing game!")
max_guesses = int(input("Enter the maximum number of guesses allowed "))               # part (iv)
game_diff = str(input("Enter difficulty E(asy) or H(ard): "))                          # part (v)
guess_game(max_guesses, game_diff)                                                     # part (iv), (v)
