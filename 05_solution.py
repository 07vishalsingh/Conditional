'''
(5).Problem: Suggest an activity based on weather(e.g.,Sunday-go for a walk,Rainy-Read a book,Snowy-Build a snowman).
'''

weather = input("Today's weather is:")

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Solve Python question"
elif weather == "snowy":
    activity = "Build a snowman"
    
print(activity)
    
   
    