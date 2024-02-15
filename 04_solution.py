'''   
(4). Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.(eg.Banana;Green-Unripe,Yellow-Ripe,Brown-Overripe)
'''
   
# fruit = "Banana"  
# color = "Green"  

# if fruit == 'Banana':
#    if color == 'Green':
#        print("Unripe")

#    elif color == 'Yellow':
#        print('Ripe')
#    elif color == 'Brown':
#        print("OverRipe")
   
fruit = (input("Enter the fruit name:"))
color = input("Enter the color name :")

if fruit == "Banana":
    if color == "Green":
        print("Fruit is Unripe")
    elif color == "Yellow":
        print("Fruit is Ripe")
    elif color == "Brown":
        print("Fruit is OverRipe")
   

    