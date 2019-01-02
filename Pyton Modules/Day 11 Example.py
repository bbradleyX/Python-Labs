'''
num=int(input("Enter an integer:"))
symbol="*"
count=0
space=" "
count2=num
while(num>count):
    star=1
    while(count2>=0):
        count2=count2-1
    while(count<=num):
        print(symbol*star)
        star=star+2
        count=count+1

size=int(input("Enter the size please:"))
count=1
stars=-1
while(count<=size):
    spaces=size-count
    stars=stars+2
    print(str(count)+" "+str(spaces)+" "+str(stars))
    count=count+1
'''
size=int(input("Enter the size please:"))
count=1
stars=-1
while(count<=size):
    spaces=size-count
    stars=stars+2
    count2=0
    outStr=''
    while(count2<spaces):
        outStr=outStr+"*"
        count2=count2+1
    count2=0
    while(count2<stars):
         outStr=outStr+"*"
         count2=count2+1
         print(outStr)
    print(str(count)+" "+str(spaces)+" "+str(stars))
    count=count+1
