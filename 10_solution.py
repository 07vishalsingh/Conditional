'''
(10).Problem: Recommended a type of pet food based on the pet's species and age.(eg.,Dog:<2years-puppy food,cat:>5years-senior cat food)
'''
species = input("Enter the species of your pet (dog/cat): ").lower()
age = int(input("Enter the age of your pet: "))

food = "generic pet food"

if species == "dog":
    if age < 2:
        food = "puppy food"
    elif age >= 2 and age <= 5:
        food = "adult dog food"
    elif age > 5:
        food = "senior dog food"
elif species == "cat":
    if age < 2:
        food = "kitten food"
    elif age >= 2 and age <= 5:
        food = "adult cat food"
    elif age > 5:
        food = "senior cat food"

print("Recommended pet food for your", species, "is:", food)

