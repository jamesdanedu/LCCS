# Question 16(a)
# Examination Number:
from random import randint

print("Dice simulation and analysis program")   #part (i)
results = []
frequencies = [0, 0, 0, 0, 0, 0]

# Loop 100 times
for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results

    # Start to build up a list of frequencies for each value thrown
    if throw_result == 1:
        frequencies[0] = frequencies[0] + 1
    elif throw_result == 2:
        frequencies[1] = frequencies[1] + 1
    # part (iii) - generate the other frequencies
    elif throw_result == 3:
        frequencies[2] = frequencies[2] + 1
    elif throw_result == 4:
        frequencies[3] = frequencies[3] + 1
    elif throw_result == 5:
        frequencies[4] = frequencies[4] + 1
    elif throw_result == 6:
        frequencies[5] = frequencies[5] + 1

print()
#print("Results:", results)  # part (iv) comment out the results
print()
# part (v) tabulate the frequencies
print("Frequencies:", frequencies)
print("Dice Frequency")
print("==============")
for freq in range(0,6):
    print(freq+1, " ", frequencies[freq])
    
maxFreq = max(frequencies)
winningNumber = frequencies.index(maxFreq)
print(winningNumber+1, "was rolled the most often (", maxFreq, "times)")

# part (v)
print("")
starString=""
for freq in frequencies:
    for i in range(0,freq):
        starString = starString + "*"
    print(starString)
    starString = ""
