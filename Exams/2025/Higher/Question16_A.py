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
    
    





