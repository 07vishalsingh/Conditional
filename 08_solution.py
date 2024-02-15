'''
(8).Problem: Check if a password is "weak",or "Strong". Criteria:<6 chars(weak),6-10 chars(Medium), >10 chars(strong).

'''
password = input("Enter your password:")
password_length = len(password)

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "medium"
else:
    strength = "strong"    
print("Password strength is:", strength)    