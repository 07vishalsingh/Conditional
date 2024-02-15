'''  
1. Age group Categorization.
classify a person's age group: Child(1<13),Teenager(13,19),Adult(20-59),Senior(60+)

'''
age = int(input('Provide me your age:'))

if age < 13 and age >= 1:
    print("Child")
elif age < 19 and age >= 13:
    print("Teenager")
elif age < 60 and age >= 20:
    print("Adult")
else:
    print("Senior")
