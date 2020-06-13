# 1.Write a program that takes your result and show your cgpa.
# Sample input:
# enter your result: 80
# sample output:
# your marks is 80 and you got A+

mark = float(input("Enter Your Score/Mark: "))
if mark >= 0 and mark <= 100 :
    if mark >= 0 and mark <= 33:
        print("Your Score is {} and you got F Grade".format(mark))
    elif mark >= 34 and mark <= 40:
        print("Your Score is {} and you got E Grade".format(mark))
    elif mark >= 41 and mark <= 50:
        print("Your Score is {} and you got D Grade".format(mark))
    elif mark >= 51 and mark <= 60:
        print("Your Score is {} and you got C Grade".format(mark))
    elif mark >= 61 and mark <= 70:
        print("Your Score is {} and you got B Grade".format(mark))
    elif mark >= 71 and mark <= 79:
        print("Your Score is {} and you got A Grade".format(mark))
    else:
        print("Your Score is {} and you got A+ Grade".format(mark))
else:
    print("INVALID! Enter Score in between 0 and 100. ")