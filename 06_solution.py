'''
(6).Problem: Choose a mode of transportation based on the distance(e.g., <3 km: Walk,3-15km:Bike,>15km:car).

'''
distance = int(input("Enter the total distance:"))

if distance < 3:
    transportation = "Walk"
elif distance <=15 and distance > 3:
    transportation = "Bike"
else:
    transportation = "Car"
print(transportation)    
    