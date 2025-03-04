


print(len(input("What is your name ?")))

username = (input("What is your name ?"))
length = len(username)

print(length)

print("Welcome to the door")
input("city name ? \n ")
input("pet name? \n ")
input("Bnd name? \n ")


print("Welcome to tip calculator")
total_bill = float(input("What was the total bill? \n "))
tip = int(input("How much tip would you like to give 10,15 or 20? \n "))
split = int(input("How many people to split the bill? \n "))

balance = total_bill + tip
pay = ( balance / split)
print(f"Each Person should Pay:- ₹ {pay}" )

print("Hello" [2])


print(type(123))
print(type("Hello"))
print(type(54.6))
print(type(False))

print(3 * 3 + 3 / 3 - 3 )

height = 1.65
weight = 65
# height = input("Your Height")
# weight = input("Your weight")


bmi = weight / height

  print(bmi)

    print("Welcome to Bike Ride")
    height = int(input("Enter your height \n"))
    bill = 0

    if height >= 180:
        print("You are eligible for Ride.")
        age = int(input("Enter Your Age \n"))

        if age <= 12:
            bill = 10
            print("You have to Par 10 Rupees")
        elif age <= 18:
            bill = 15
            print("You Have to Pay 15 Rupees")
        else:
            bill = 20
            print("You Have to pay 20 Rupees")

            wants_Photo = input("If you want a pic then type Y otherwise type N \n")
            if wants_Photo == "y":
                bill += 3
            print(f"Your final bill is {bill}")

    else:
        print("Sorry you are not eligible.")

    number_check = int(input("Enter Your Number \n"))

    if number_check % 2 == 0:
        print("Even")
    else:
        print("Odd")

    print("Welcome to Treasure island")
    print("Your mission is to fine the Treasure")

    choice1 = input(' Where do you want to go? Type "Left" or "Right"\n').lower()
    if choice1 == "left":
        choice2 = input('Middle of lake.Type "Wait" or "swim"\n')
        if choice2 == "wait":
            choice3 = input(
                "You are arrive at the island unharmed. There is house 3 doors. One Red ,one Yellow and One Blue. which color would you choose\n").lower()
            if choice3 == "red":
                print("Game Over")
            elif choice3 == "Yellow":
                print("You Win")
            elif choice3 == "Blue":
                print("Game Over")
            else:
                print("Door dont exist")
        else:
            print("You got attacked by angry trout, game Over\n")
    else:
        print("You fell into a hole.Game over")




import random

random_integer = random.randint(0,1)
if random_integer == 0:
    print("Head")
else:
    print("Tail")


    # import random
#
# friends = ["Ramesh","Suresh","Yogesh","Sukesh","Mukesh"]
#
# # 1st option
# random_index = random.randint(0,4)
# print(friends[random_index])
#
# # 2nd option
# print(random.choice(friends))


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozon = [fruits,vegetables]
#
# print(dirty_dozon[1][1])
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

import random
user_choice = int(input("What user choose \n"))
computer_choice = random.randint(0,2)
print(f'computer choice {computer_choice}')

if user_choice >= 3 and computer_choice < 0:
    print("You Won!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win")
elif computer_choice == user_choice:
    print("Draw!")
else:
    print("Enter valid Number")