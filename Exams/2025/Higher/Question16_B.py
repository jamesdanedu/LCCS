
def calcMedian(numList):
    if not numList:
        print("Error, list is empty, cannot calculate median")
        return None
    
    numList.sort()  # should do this in the general case, it is already done in the main codeline here, but
                    # it needs to be done to make the function generally useful
    
    lenList = len(numList)
    #if length of list is odd
    if lenList % 2 == 1:
        # This means there is one middle number, so lets find it
        middlePos = lenList // 2
        return numList[middlePos]
    else:
        firstMiddlePos = lenList // 2
        secondMiddlePos = (lenList // 2)-1
        return (numList[firstMiddlePos] + numList[secondMiddlePos])/2


# initialise list of numbers
numberList_1 = [11, 12, 14, 16, 16, 19, 21, 14, 13, 15, 16]
numberList_2 = [11, 12, 14, 16, 16, 19, 20, 21, 14, 13, 15, 16]

emptyList = []

# print the list
print("The list of unsorted numbers is ", numberList_1)
print("The list of unsorted numbers is ", numberList_2)

# sort the list
numberList_1.sort()
numberList_2.sort()

# print the sort list
print("The list of sorted numbers is ", numberList_1)
print("The list of sorted numbers is ", numberList_2)


# Determine the median
median = calcMedian(numberList_1)
print("The median of an odd list of numbers is", median)


median = calcMedian(numberList_2)
print("The median of an even list of numbers is", median)

# Ensure an error is reported
median = calcMedian(emptyList)

