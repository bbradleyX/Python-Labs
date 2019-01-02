'''
Bria Bradley
Date: 9/29/17
HW9
'''
#1:print all the numbers from 1 to 20
num=0
newnum=num+1
print(newnum)
while(newnum<20):
    newnum=newnum+1
    print(newnum)
#2:print all the numbers from 1 to a positive number entered by the user
num=0
newnum=num+1
userInput=int(input("Enter a positive number:"))
print(newnum)
while(userInput!=newnum):
    newnum=newnum+1
    print(newnum)
#3:print all the numbers from a positive number entered by the user down to 1
userInput=int(input("Enter a positive number:"))
print(userInput)
num=userInput
newnum=num-1
while(newnum>1):
    newnum=newnum-1
    print(newnum)
#4:print all the even numbers from 2 to a positive number entered by the user
num=0
newnum=num+2
userInput=int(input("Enter a positive number:"))
evenTest=userInput/2
if evenTest-int(evenTest)!=0:
    print("not an even number")
else:
    while(userInput!=newnum):
        newnum=newnum+2
        print(newnum)
#5:print each string the user enters until they enter “quit” (don't print quit)
userInput=str(input("Say what you want:"))
while(userInput!="quit"):
    print(userInput)
    userInput=str(input("Say what you want:"))
#6:print each string the user enters until they enter “quit” or “QUIT” or “Quit” (don't print quit)
userInput=str(input("Say what you want:"))
while(userInput!="quit"and userInput!="Quit" and userInput!="QUIT"):
    print(userInput)
    userInput=str(input("Say what you want:"))  
#7:repeatedly ask the user for a positive number until they enter a positive number
userInput=int(input("Enter a positive number:"))
evenTest=userInput/2
while(evenTest-int(evenTest)!=0):
     print("not an even number")
     userInput=int(input("Enter a positive number:"))
#8:add all the numbers between 0 and a positive number entered by the user and print the result (you can assume that the user enters a positive number)
num=0
newnum=num+1
userInput=int(input("Enter a positive number:"))
while(newnum<=userInput):
    total=newnum+num
    num=total
    newnum=newnum+1
print(total)
