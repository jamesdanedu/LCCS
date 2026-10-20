# Question 16(b)
# Examination Number:

from random import choice

fruitList = ['apple', 'cherry', 'orange']
print("The initial list of fruits is", fruitList)

additionalFruit = input("Enter an additional fruit ")
fruitList.append(additionalFruit)    #add the additional fruit to the list

print("The list of four fruits is", fruitList)



winningFruit = input("Nominate your winning fruit ")
# Where the user hasnt entered a fruit thats in the list
while winningFruit not in fruitList:
    # report the error and keep asking the user for a correct entry
    print("Error, this item (",winningFruit,") is not in the list, try again")
    winningFruit = input("Nominate your winning fruit ")

print("The winning fruit you selected is", winningFruit)
tryCount=0    # track the number of tries (or games) played
threeMatchesFound = False     #track when we have found three matching fruits
while threeMatchesFound == False:
    fruit1 = choice(fruitList)
    fruit2 = choice(fruitList)
    fruit3 = choice(fruitList)
    # If all fruits are matching and its matching the winning fruit
    if winningFruit == fruit1 and fruit1 == fruit2 and fruit1 == fruit3:
        threeMatchesFound = True
    #print("Variables:", fruit1, fruit2, fruit3)
    tryCount = tryCount + 1

print("Winner after", tryCount, " tries")

