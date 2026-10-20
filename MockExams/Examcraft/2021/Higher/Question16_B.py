# Question 16(b)
# examination Number:

studentNames = []
studentGrades = []

# Add students onto a list
def addStudents():
    studentName = "NotEnd"
    while studentName != "end" and studentName != "End":
        studentName = input("Please enter the students name and enter 'end' or 'End' when complete ")
        if studentName != "end" and studentName != "End":
            studentNames.append(studentName)
    return len(studentNames)

# Add as many grades onto a list as there are students already created
def addGrades(studentCount):
    studentGrade = -2
    gradeInputs = 0
    # gradeInputs not needed for the exam - but its good defensive programming, preventing 
    # users making a mistake and inadvertently entering extra grades
    while studentGrade != -1 and gradeInputs < studentCount:   
        studentGrade = int(input("Please enter the students grade and enter '-1' when complete "))
        if studentGrade != -1:
            studentGrades.append(studentGrade)
            gradeInputs = gradeInputs + 1

    return len(studentGrades)


# Main program
studentCount = addStudents()
print("You added", studentCount, "students:", studentNames)
gradeCount = addGrades(studentCount)
if gradeCount != studentCount:
    print ("Error - you havent entered same number of names and grades, program ending")
else:
    print("Grade summary:")
    for stu in range(0,len(studentNames),1):
        print("[[",studentNames[stu],",",studentGrades[stu],"]]")

    maxScore = max(studentGrades)
    minScore = min(studentGrades)
    avgScore = (sum(studentGrades)/len(studentGrades))

    print("Highest score (%)", round((maxScore/200)*100,1), "%")
    print("Lowest score (%)", round((minScore/200)*100,1), "%")
    print("Average score (%)", round((avgScore/200)*100,1), "%")


    print("The student who scored the highest value is:", studentNames[studentGrades.index(maxScore)])
    print("The student who scored the lowest value is:", studentNames[studentGrades.index(minScore)])
    



