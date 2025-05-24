# Question 16 (a)
# Examination Number:

def get_grade(result):
    grade = "Unsuccessful"
    
    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    elif result >= 50:		#part (iii)
        grade = "Lower Merit"		#part (iii)
    elif result >= 40:		#part (iii)
        grade = "Pass"		#part (iii)

    return grade


#part (v) Min and Max Functions
def getMinGrade(results):
    if not results:
        return None
    return min(results)

def getMaxGrade(results):
    if not results:
        return None
    return max(results)

#part (iv) 
def getLTCount(targetNum, results):
    if not results:
        return None
    ltCount = 0
    for i in results:
        if i < targetNum:
            ltCount += 1
            
    return ltCount

def getIBTWCount(targetLowNum, targetHighNum, results):
    if not results:
        return None
    ibtwCount = 0
    for i in results:
        if targetLowNum <= i <= targetHighNum: 
            ibtwCount += 1
            
    return ibtwCount

# end part (iv)


# part (vi)
def findLongestIncreasingRun(results):
    if not results:
        return None
    
    currentRun = [results[0]]
    longestRun = [results[0]]
    
    for i in range (1, len(results)):
        if results[i] > currentRun[-1]:
            currentRun.append(results[i])
        else:
            if len(currentRun) > len(longestRun):
                longestRun = currentRun[:]
            currentRun = [results[i]]
    
    if len(longestRun) < 2:
        return None
    else:
        return longestRun
    
    

# Calculate and display the mean of a list of results
results = [39,32,62,88,51,62,64,81,77] # Initialise the list
N = len(results) # Initialise N to the number of results
total = 0 # Initialise the running total to 0

# Loop N times
for i in range(N):
    total = total + results[i] # Running total

# Divide by the total number of results to give the mean
#arithmetic_mean = total/9

#part (ii)
arithmetic_mean = total/N


# Display the answer
# Part (i)
print(f"The mean percentage mark is {arithmetic_mean:.2f}")

# part (iv)
print("The grade for the average result is", get_grade(arithmetic_mean))

# part (v)
print("The lowest score is:", getMinGrade(results))

print("The highest score is:", getMaxGrade(results))

# part (vi)
print("The number of scores below 40 is", getLTCount(40, results))
print("The number of scores between 50 and 79 inclusive is", getIBTWCount(50, 79, results))

# part (vii)
print("The longest run of result increases is", findLongestIncreasingRun(results))




