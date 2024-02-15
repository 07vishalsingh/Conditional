'''
(7).Problem: Customize a coffee order: 'small','medium',or 'large' with an option for 'extra shot' of espresso.

'''

order_size = input("Enter your preference for coffee:")

extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"
print("Order:", coffee)    