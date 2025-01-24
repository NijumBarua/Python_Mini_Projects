import random
Choice_List = ["Rock" , "Paper" , "Scissor"]
Choice_fuction = str(input("Choose any of this [Rock , Paper , Scissor ] and write in the same was as it shown: "))

Comp_choice = random.choice(Choice_List)

print(f"Your choice {Choice_fuction} and comupter choice is {Comp_choice}")

if Choice_fuction == Comp_choice :
    print("Both choosed the same , so it's a tie")

elif Choice_fuction == "Rock":
    if Comp_choice == "Scissor":
        print("You win!!!  , Rock beats up scissors")
    else :
        print("Computer WIN!!! , Paper covered rock ")

elif Choice_fuction == "Scissor":
    if Comp_choice == "Paper":
        print("YOU WIN!!!!  , Scissor cuts Paper ")
    else :
        print("Computer WON!!! , Rock beats up scissors ")

elif Choice_fuction == "Paper":
    if Comp_choice == "Rock":
        print("You WON!!!  , Paper covered rock")
    else :
        print("Computer win!!! , Scissor cuts Paper ")

