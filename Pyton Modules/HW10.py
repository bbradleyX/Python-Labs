'''
n=1
while(n<6):
    m=1
    while(m<6):
        p=m*n
        print(p, end='')
        m=m+1
    print()
    n=n+1
'''
#This code is backwards...had trouble figuring out how to reverse the plus output
num=int(input("Enter an integer:"))
count=1
plus="+"
while(count<=num):
    print(count)
    count=count+1
    count2=count-1
    while(count2<=num):
        print(plus)
        count2=count2+1
num=int(input("Enter an integer:"))
symbol="*"
count=0
while(num>=0):
    while(count<=num):
        print(symbol*count)
        count=count+1
    num=num-1

