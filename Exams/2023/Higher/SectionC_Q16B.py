# Q16B
# Examination Number:  <enter your exam number here!>

from random import randint

score = 0
totalScore = 0

def guess_round(user_guess: int) -> int:
  secret_number = randint(1, 100)
  differ = abs(secret_number-user_guess)
  print("Secret number is ",secret_number, ", You guessed ", user_guess, ". Difference is ",differ)
  if (secret_number == user_guess):
    print("JACKPOT!!! You score 100 points")
    return 100
  elif ( differ <= 20 ):
    print("You score 20 points")
    return 20
  elif ( differ > 30 ):
    print("You score -30 points")
    return -30

  
  
print("Welcome to the guessing game!")
play_again = 'Y'
while (play_again == 'Y'):
  your_guess = (int)(input("Enter your guess: "))
  score = guess_round(your_guess)
  totalScore = totalScore + score
  print("Your total score is ", totalScore)
  play_again = (str)(input("Play again? Y/N" ))
