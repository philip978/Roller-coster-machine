print("You wanna ride!?")
height = int(input("what is your height?"))
age = int(input("what is your age?"))
photo = input("do you want photo?")
bill = 0
if height > 120:
    print("can ride")
    if age < 12:
        bill = 5
    elif 12 < age < 18:
        bill = 7
    elif age > 18:
        bill = 12
    if photo == "y":
        bill += 3
    if 45 <= age <= 55:
        bill = 0

else:
    print("wait till you go grow taller")
print(f"final bill is {bill}")
