# Question 16(a)
# Student Name:


# (iv) print user name message
def username():
    student_name=input("Please enter the students name: ")
    print("Welcome", student_name, "to the student result calculation")
    return student_name

# (v) showStudentResults as a category
def showStudentResults(grade):
    if grade > 100 or grade < 0:
        print("Error invalid grade")
        officialGrade = 'Error'
    elif grade >= 80 and grade <= 100:
        officialGrade = 'A'
    elif grade >= 60 and grade <= 79:
        officialGrade = 'B'
    elif grade >= 0 and grade <= 59:
        officialGrade = 'C'
    else:
        print("Logic error")
    return officialGrade
   
studentName = username() # (iv) call to function
#(i)  Change int to float
student_score=float(input("Please enter the students mark: "))
#(ii) exam_total
exam_total=int(input("Please enter the total amount of marks going for the exam: "))
score_as_a_percentage=(student_score/exam_total)*100
#(iii) round number to 1 decimal place
#(vi) call to showStudentResults function
print(studentName,"scored",round(score_as_a_percentage,1),"%,", "they got a", showStudentResults(score_as_a_percentage))



