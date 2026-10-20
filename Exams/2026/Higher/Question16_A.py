# Question 16 (a)
# Examination Number:

VOWELS = "aeiou"


# part (vii) - estimate syllables: count vowels, minus 1 for a silent 'e' at the end
def count_syllables(word):
    word = word.lower()
    syllables = 0
    for letter in word:
        if letter in VOWELS:
            syllables = syllables + 1
    if word.endswith("e"):
        syllables = syllables - 1
    return syllables


# Function to calculate readability score of text
def calculate_readability_score(text):

    # Split the text into a list of words
    words = text.split()
    print("The list of words in the text is:\n", words)

    # Initialise the word counters
    word_count = len(words) # Number of words in list
    short_word_count = 0
    complex_word_count = 0                              # part (vii)

    # part (v) and (vii) - count short words and complex words
    for word in words:
        if len(word) <= 2:
            short_word_count = short_word_count + 1
        if count_syllables(word) >= 3:
            complex_word_count = complex_word_count + 1
    print("Short Words:", short_word_count)            # part (v)
    print("Complex Words:", complex_word_count)        # part (vii)

    # Initialise the number of sentences
    # part (iii) - exclamation marks also end a sentence
    sentence_count = text.count(".") + text.count("!")

    # Calculate the readability score
    # part (vi) - new formula replaces word_count * sentence_count
    score = 0.4 * ((word_count / sentence_count) +
                   100 * ((word_count - short_word_count) / word_count))
    score = round(score, 2) # Round the score to 2 d.p.

    return score

# Set the text for analysis
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways."
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"

# Calculate the score for text1
score1 = calculate_readability_score(text1)
print("Readability Score 1:", score1)      # part (i)
print()                                     # part (i) blank line

# part (ii) - calculate and display the score for text2
score2 = calculate_readability_score(text2)
print("Readability Score 2:", score2)
print()

# part (iv) - compare the two scores
if score1 == score2:
    print("Both scores are the same.")
elif score1 < score2:
    print("The first text is easier to read.")
else:
    print("The second text is easier to read.")
