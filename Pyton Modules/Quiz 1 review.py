'''
WHILE LOOPS
initialize variable
while(variables):
    do something
    update variables
'''
'''
#first example
num1=int(input("enter an integer: "))
num2=int(input("enter another integer: "))
while(num1*num2!=0):
    print(num1*num2)
    num1=int(input("enter an integer: "))
    num2=int(input("enter another integer: "))
'''
'''
#if the 1st num1>0 then it will skip 1st while loop
num1=int(input("enter an integer: "))
#fixing num1 variable by acting as a "gate keeper", can't get past this code until num>0
#only place inside while loops what you want to be repeated
while(num1<0):
    num1=int(input("enter a positive integer: "))
num2=int(input("enter another integer: "))
while(num1<0):
    num1=int(input("enter a positive integer: "))
    num2=int(input("enter another integer: "))

while(num1*num2!=0):
    print(num1*num2)
    num1=int(input("enter an integer: "))
    while(num1<0):
        num1=int(input("enter a positive integer: "))
    num2=int(input("enter another integer: "))
    while(num2<0):
        num2=int(input("enter another integer: "))

#use if statments to branch off of while loops
num1=int(input("enter an integer: "))
while(num1<0):
    num1=int(input("enter a positive integer: "))
num2=int(input("enter another integer: "))
while(num1<0):
    num1=int(input("enter a positive integer: "))
    num2=int(input("enter another integer: "))
while(num1*num2!=0):
    amount=num1*num2)
    if(amount>100):
        print("wow")
    num1=int(input("enter an integer: "))
    while(num1<0):
        num1=int(input("enter a positive integer: "))
    num2=int(input("enter another integer: "))
    while(num2<0):
        num2=int(input("enter another integer: "))
'''
'''
name=input("who is your coolest professor")
while(name!="Paul"):
    name=input("No, I said who is your coolest professor?")
print("why thank you I'm flattered")
'''
n=1
while(n<6):
    m=1
    print()
    n=n+1
