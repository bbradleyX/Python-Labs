'''
num1=int(input("Enter a number:"))
num1=int(input("Enter another number:"))
num=0
newnum=num+1
print(newnum)
while(newnum>=num1 and newnum<=num2):
    newnum=newnum+1
    print(newnum)
'''
##num1=1
##num2=6
'''
again="y"
while(again=="y"):
    num1=int(input("Enter#:"))
    num2=int(input("Enter another #:"))
    if(num1<num2):
        while(num1<=num2):
            print(num1)
            num1=num1+1
    else:
         while(num1<=num2):
            print(num1)
            num1=num1+1
    again=input("Want to go again(y/n)?")
'''
#newnum is the same as saying count
num=int(input("Enter an integer:"))
count=1
while(count<=5):
    count=count+1
    print(num,end="")
'''
num=int(input("Enter an integer:"))
count=1
while(count<=num):
    count2=0
    while(count2<num):
        print(count,end="")
        count2=count2+1
    print()
    count=count+1
'''
