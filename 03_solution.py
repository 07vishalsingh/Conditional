'''   
(3). Problem: Assign a letter grade based on a student's score: A(90-100),B(80-89),C(70-79),D(60-69),F(BELOW 60).
'''
# score = 89
# if score >= 101:
#    print("Please verify your grade again")  
#    exit()  
#
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"
#     print("Grade:", grade)
    
marks = int(input("Enter your Marks:"))

if marks < 100 and marks >= 90:
     print("Your Grade is A")
elif marks < 90 and marks >= 80:
     print("Your Grade is B")
elif marks < 80 and marks >= 70:
     print("Your Grade is C")
elif marks < 70 and marks >= 60:
    print("Your Grade is D")
else:
     print("Your Grade is F")
   