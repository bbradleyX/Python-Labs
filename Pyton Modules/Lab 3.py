'''
#Bria Bradley
#Date: 9/26/17
#Purpose: Use of if statements to determine customer's order
'''
age=int (input ("Enter your age:"))
print ("Choose meal number: \n 1. Fish and vegetables \n 2. Steak and baked potato \n 3. Burger and fries")
food=int (input ("Enter meal number:"))
if food==1 and age<21:
    print ("order: fish and vegetables with ice tea")
elif food==1 and age>=21:
    drink=(str(input("Choose drink, ice tea or white wine:")))
    if drink=="ice tea":
        print ("order: fish and vegetables with ice tea")
    elif drink=="white wine":
        print ("order: fish and vegetables with white wine")
elif food==2 and age<21:
    print ("order: steak and baked potato with lemonade")
elif food==2 and age>=21:
    drink=str (input ("Choose drink option, lemonade or red wine:"))
    if drink=="lemonade":
        print ("order: steak and baked potato with lemonade")
    elif drink=="red wine":
        print ("your order: steak and baked potato with red wine")
elif food==3 and age<21:
    print ("order: burger and fries with cola")
elif food==3 and age>=21:
    drink=str(input ("Choose drink option, cola or beer"))
    if drink=="cola":
        print ("order: burger and fries with cola")
    elif drink=="beer":
        print ("your order: burger and fries with beer")
else:
    print("not a meal option")
