# Create a Python Program that perform following tasks for any problem of your choice:
# ____________________________________________________________________________________
def printresult(coursesandmarks, gpalist, gpa):
    print("____Result____")
    for i in range(len(coursesandmarks)):
        print(coursesandmarks[i][0], '\t',
              coursesandmarks[i][1], '\t', gpalist[i])
    print("Cumulative Gpa is ", gpa)

def calculategpa(marks):
    gpalist = []
    for i in range(len(marks)):
        mark = marks[i][1]
        gpa = 0
        if (mark >= 85):
            gpa = 4.0
        elif (mark >= 80 and mark <= 84):
            gpa = 3.8
        elif (mark >= 75 and mark <= 79):
            gpa = 3.4
        elif (mark >= 71 and mark <= 74):
            gpa = 3.0
        elif (mark >= 68 and mark <= 70):
            gpa = 2.8
        elif (mark >= 64 and mark <= 67):
            gpa = 2.4
        elif (mark >= 61 and mark <= 63):
            gpa = 2.0
        elif (mark >= 57 and mark <= 60):
            gpa = 1.8
        elif (mark >= 53 and mark <= 56):
            gpa = 1.4
        elif (mark >= 45 and mark <= 52):
            gpa = 1.0
        gpalist.append(gpa)
    totalgpa = 0
    for i in range(len(gpalist)):
        totalgpa += gpalist[i]
    totalgpa /= len(gpalist)
    printresult(marks, gpalist, totalgpa)

print("____GPA Calculator____")
n = int(input("Enter the number of subject: "))
if (n <= 0):
    print("Sorry!! You must have atleast one subject to calculate gpa")
else:
    coursesandmarks = []
    while (n > 0):
        course = input("Enter course name: ")
        marks = float(input("Enter marks: "))
        n -= 1
        coursesandmarks.append((course, marks))
calculategpa(coursesandmarks)
