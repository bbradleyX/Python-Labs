##thereYet="no"
##while(thereYet=="no"):
##    print("drive, drivey, drive")
##    thereYet=input("Are we there yet?: ")
##print("Arrived!")
##largest=10
##total=0
##current=1
##while (current<=largest):
##    total=total+current
##    current=current+1
##print(total)
#Take numbers from users until said "done" and take average
#convert to a float after "done" comparison
'''
userInput=input("Enter a number or type done to finish: ")
count=0
total=0
while (userInput!="done"):
    userInput=float(userInput)
    total=total+userInput
    count=count+1
    average=total/count
    userInput=input("Enter a number or type done to finish: ")
print(average)
'''
#Determine which number is max/min after user enter numbers until said done
userInput=input("Enter a number or done:")
userNum=int(userInput)
small=userNum
big=userNum

while(userInput!="done"):
    userNum=int(userInput)
    if(userNum<small):
        small=userNum
    elif(userNum>big):
        big=userNum
    userInput=input("Enter a number or done:")
print("Small number is: "+str(small))
print("Big number is:"+str(big))
