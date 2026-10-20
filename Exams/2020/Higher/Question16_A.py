# Question 16(a)
# Examination Number:

# Prompt the user to enter a password and store the ...
# value entered in the variable password
password = input("Enter a password: ")
print("Password :", password)   # part (ii)

# A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = LOWER_CASE_LETTERS.upper()   #part (iii)

# The variables lowercase and uppercase indicate the presence or ...
# absence of lowercase and uppercase characters in the password
lowercase = False # True if password contains a lowercase letter
uppercase = False # True if password contains an uppercase letter

# Loop through each character in the password and ...
# check the password for specific  characters
for character in password:
    if character in LOWER_CASE_LETTERS:
        lowercase = True
    if character in UPPER_CASE_LETTERS:		# part (iii)
        uppercase = True
        
# Calculate the score based on the rules

score = 0    # part (i)

# Rule 1    # part 
if len(password) > 7:
    score = score + 5
elif len(password) >= 4 <= 7:
    score = score + 2
elif len(password) < 4:
    score = score - 2

# Rule 2
if lowercase:
    score = score + 1

# Rule 3
if lowercase and uppercase:
    score = score + 5

#part (iv)
# Rule 4
if uppercase:
    score = score + 2

#part (v)
#Rule 5
digitCount=0
for i in password:
    if (i.isdigit()):
        digitCount=digitCount+1
if digitCount >= 1:
    score = score + 5    
    #part (vi)
    firstCharIsDigit=False
    lastCharIsDigit=False
    if password[0].isdigit():
        score = score + 1
        firstCharIsDigit = True
    if password[-1].isdigit():
        score = score + 1
        lastCharIsDigit = True
    if firstCharIsDigit and lastCharIsDigit:
        score = score + 2
    # part (vii)
    # Rule 7
    #If there are not alphabetic characters
    if not lowercase and not uppercase:
        score = score - 10
        
# Display the score
print("Score: ", score)    #part (ii)

