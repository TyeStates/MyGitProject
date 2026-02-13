import gradespy

def enterWeights():
    #Takes user input to decide the percentage weights for each possible mark
    #if the user does not have a mark with this type, they should simply enter a 0
    #does not allow user to input a total weight greater than 100%
    #returns a list of the weights as integers
    while(True):
        total = 0
        
        assignWgt = int(input("Enter your assignment weight: "))
        quizWgt = int(input("enter your quiz weight: "))
        testWgt = int(input("Enter your test weight: "))
        mtWgt = int(input("Enter your midterm weight: "))
        examWgt = int(input("Enter your exam weight: "))
        projWgt = int(input("Enter your project weight: "))
        returnable = [assignWgt, quizWgt, testWgt, mtWgt, examWgt, projWgt]
        
        for item in returnable:
            total += item

        if total == 100:
            break
        else:
            print("Marks should add up to 100%, yours add up to {total}%\n please reenter weights.")
    return returnable

# used for simplicity of working with confirmations
markTypes = ["assignment", "quiz", "test", "midterm", "exam", "project"]
# menu exit condition for program.
ExitCondition = False
print("Grade Calculator:")


while(ExitCondition == False):
    print("To begin, let's enter the weights")

    weights = enterWeights()
    
    # prints the weights with their assigned percentages and types
    for i in range(len(weights)):
        if(weights[i] > 0):
            print(f"{markTypes[i]} weight = {weights[i]}%")
    print("is this correct?")

    yesOrNo = input("enter a 0 for 'no' and anything else for 'yes': ")  
    if(yesOrNo != 0):
        ExitCondition = True
ExitCondition = False

grades = []
for i in range(len(weights)):
    if weights[i] > 0:
        count = int(input(f"enter the amount of {markTypes[i]}s you have: "))
        for j in range(1, count+1):
            score = float(input(f"enter the grade you got on {markTypes[i]}{j}: "))
            grades.append(gradespy.Grade(markTypes[i], score, weights[i]))

finalGrade = gradespy.calc_final_grade(grades, weights)
print(f"your final grade as of now would be {finalGrade}")

            
