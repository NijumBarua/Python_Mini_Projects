# In this project we are doing a cafe management system where we take orders from the user and make a bill for him and finally supply
#We are using a dictionary for this project And conditional statements
Menu = {
    'Domino.s Pizza (1 full)': 250 ,
    'Burger King (1 piece)': 300,
    'Pasta (1 plate)' : 200,
    'Coffee' : 80,
    'Tea' : 20,
    'Mixed Salad': 50,

}

print("                WELCOME TO MOTI MAMAR KHABAR DABAR            \n                      Ekbar Kheyei Dekhen")
                                 



print(" Domino.s Pizza (1 full): 250 Taka \n Burger King (1 piece): 300Taka\n Pasta (1 plate) : 200Taka\n Coffee : 80Taka\n Tea : 20Taka\n Mixed Salad: 50Taka ")

order = 0

item_1 = input('Enter the item you want to order : ')
if item_1 in Menu:
    order += Menu[item_1] #It will store the amount of taka that will be added for the final payment
    print(f"Your First order {item_1} has been taken ")

else:
    print(f"Your ordered {item_1} is not available right now")

Added_Order = input('Do you add another item?? (Yes/No) : ')
if Added_Order == "Yes":
    item_2 = input('Enter the added item  you want to order : ')
    if item_2 in Menu:
     order += Menu[item_2] #It will store the amount of taka that will be added for the final payment
     print(f"Your added {item_2} has been taken ")

    else:
      print(f"Your ordered {item_2} is not available right now")

print("Your order on the way to serve")
print(f"Your total amount of {order} has to pay , Now Enjoyyyyyyyyyyyyyyyy!!!!")



