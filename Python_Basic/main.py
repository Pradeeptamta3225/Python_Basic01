


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