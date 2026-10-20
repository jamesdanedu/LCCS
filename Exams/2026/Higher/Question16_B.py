# Question 16 (b)
# Examination Number:

# Only the letters A-Z and a-z are allowed in a word
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# Return True if the word is not empty and contains only letters A-Z / a-z
def is_valid_word(word):
    if len(word) == 0:
        return False
    for character in word:
        if character not in LETTERS:
            return False
    return True


# Score an uppercase word: vowels 1 point, V W X Y Z 5 points, other letters 3 points
def score_word(word):
    score = 0
    for letter in word:
        if letter in "AEIOU":
            score = score + 1
        elif letter in "VWXYZ":
            score = score + 5
        else:
            score = score + 3
    return score


total_score = 0         # running total across all rounds
highest_word = ""       # highest scoring word so far
highest_score = 0       # score of the highest scoring word

play_again = "Y"
while play_again == "Y" or play_again == "y":

    # Keep asking until the user enters a valid word
    word = input("Enter a word: ")
    while not is_valid_word(word):
        print("Invalid word.")
        word = input("Enter a word: ")

    # Convert to uppercase before scoring
    word = word.upper()
    word_score = score_word(word)
    total_score = total_score + word_score
    print("Word: " + word + ", Score: " + str(word_score) + ", Total score: " + str(total_score))

    # Track the highest scoring word (first one kept on a tie)
    if word_score > highest_score:
        highest_score = word_score
        highest_word = word

    play_again = input("Play again? [Y/N]: ")

# Game over - display the summary
print("Your total score was:", total_score)
print("The highest scoring word was " + highest_word + ", " + str(highest_score) + " points")
