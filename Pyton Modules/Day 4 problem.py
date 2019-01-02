age=int(input("Enter your age: "))
if age<18:
    print("You can't Drink or Vote")
elif age==18:
    print("You can only Vote")
elif age>18:
    print("You can Vote and Drink")
