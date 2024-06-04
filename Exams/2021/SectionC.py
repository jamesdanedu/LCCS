# Question 16(a)
# Examination Number:

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False

word1 = input("Enter the first word: ")
#word2 = "SILENT"

# part 1
word2 = input("Enter the second word: ")
# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
# part (iv) make case neutral
if sorted(word1.upper()) == sorted(word2.upper()):
    # part (ii)
    print(word1, "is an anagram of", word2)
else:
    # part (iii)
    print(word1, "is not an anagram of", word2)
# part (v) 
if is_anagram(word1.upper(), word2.upper()):
    print(word1, "is an anagram of", word2)
else:
    print(word1, "is not an anagram of", word2)

# part (vi)
phrase = input("Enter a phrase: ")
strippedPhrase = phrase.replace(" ", "") 
if is_anagram(word1.upper(), strippedPhrase.upper()):
    print(word1, "is an anagram of", strippedPhrase)
else:
    print(word1, "is not an anagram of", strippedPhrase)

if is_anagram(word2.upper(), strippedPhrase.upper()):
    print(word2, "is an anagram of", strippedPhrase)
else:
    print(word2, "is not an anagram of", strippedPhrase)
    
