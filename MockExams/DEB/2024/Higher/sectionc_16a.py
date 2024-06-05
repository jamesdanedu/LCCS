import random

choices = ['rock', 'paper', 'scissors']


def play_round(player_choice, computer_choice):
  if player_choice == computer_choice:
    return 'tie'
  elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
    return 'player'
  else:
    return 'computer'

# part (ii)
def play_game(numRounds):
    playerWins = 0
    playerWinChoices = []    # part iv
    computerWins = 0
    computerWinChoices = []   # part iv
    tiedGames = 0
    tiedGameChoices = []  # part iv

    # part (i)
#    player_choice = input('Please choose rock, paper or scissors: ')
#    print('You have chosen ', player_choice)

   
    for round in range(numRounds):
        computer_choice = random.choice(choices)
        # part (iii)
        player_choice = random.choice(choices)
        roundResult = play_round(player_choice, computer_choice)
        if roundResult == 'player':
            playerWins  = playerWins + 1
            playerWinChoices.append(player_choice) # part iv
        elif roundResult == 'computer':
            computerWins = computerWins + 1
            computerWinChoices.append(computer_choice) # part iv
        else: # tie
            tiedGames = tiedGames + 1
            tiedGameChoices.append(player_choice)

    #part ii and part iii
    # print('\t\t\tOutcome')
    # print('Player win\t\t', playerWins)
    # print('Computer win\t\t', computerWins)
    # print('Tie\t\t\t', tiedGames)
    
    # part (iv)
    print('\t\t\tOutcome\tRock\tPaper\tScissors')
    print('Player win\t\t', playerWins, '\t', playerWinChoices.count("rock"),  '\t', playerWinChoices.count("paper"),  '\t', playerWinChoices.count("scissors"))
    print('Computer win\t\t', computerWins, '\t', computerWinChoices.count("rock"),  '\t', computerWinChoices.count("paper"),  '\t', computerWinChoices.count("scissors"))
    print('Tie\t\t\t', tiedGames, '\t', tiedGameChoices.count("rock"),  '\t', tiedGameChoices.count("paper"),  '\t', tiedGameChoices.count("scissors"))

    # part (v)
    # If player won more than they lost or tied
    if (playerWins > computerWins) and (playerWins > tiedGames):
        # If rock is highest scoring
        if (playerWinChoices.count("rock") > playerWinChoices.count("paper")) and (playerWinChoices.count("rock") > playerWinChoices.count("scissors")):
              print("Your winning strategy was rock, with ",playerWinChoices.count("rock"), " round wins")
        # If scissors is highest scoring
        if (playerWinChoices.count("scissors") > playerWinChoices.count("paper")) and (playerWinChoices.count("scissors") > playerWinChoices.count("rock")):
          print("Your winning strategy was scissors, with ",playerWinChoices.count("scissors"), " round wins")
        # If paper is highest scoring
        if (playerWinChoices.count("paper") > playerWinChoices.count("rock")) and (playerWinChoices.count("paper") > playerWinChoices.count("scissors")):
          print("Your winning strategy was paper, with ",playerWinChoices.count("paper"), " round wins")
    # ELSE IF computer won more than they lost or tied
    elif (computerWins > playerWins) and (computerWins > tiedGames):
        # If rock is highest scoring
        if (computerWinChoices.count("rock") > computerWinChoices.count("paper")) and (computerWinChoices.count("rock") > computerWinChoices.count("scissors")):
              print("Computer winning strategy was rock, with ",computerWinChoices.count("rock"), " round wins")
        # If scissors is highest scoring
        if (computerWinChoices.count("scissors") > computerWinChoices.count("paper")) and (computerWinChoices.count("scissors") > computerWinChoices.count("rock")):
          print("Computer winning strategy was scissors, with ",computerWinChoices.count("scissors"), " round wins")
        # If paper is highest scoring
        if (computerWinChoices.count("paper") > computerWinChoices.count("rock")) and (computerWinChoices.count("paper") > computerWinChoices.count("scissors")):
          print("Your winning strategy was paper, with ",computerWinChoices.count("paper"), " round wins") 
    else:   # More tied games than wins or losses
        print("There was more tied games than wins or losses, thus there wasnt an explicit winning strategy")
        
        
        

# part (ii)
# play_game(3)

# part (iii)
play_game(1000)




