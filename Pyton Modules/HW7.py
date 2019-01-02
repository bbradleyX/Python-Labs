num1=4
num2=2
if num1<=0:
    if num2<0:
        print("1")
    else:
        print("2")
else:
    if num2<0:
        print("3")
    else:
        print ("4")
#########################
if num1>=0:
    if num2>=0:
        print("both positive")
    elif num2==0:
        print ("one zero")
    else:
        print ("one positive")
elif num1==0:
    if num2>=0:
        print("one zero")
    elif num2==0:
        print("two zeros")
    else:
        print ("one negative")
else:
    print("at least one negative")
#####################################
scoreIn171=90
passed171=True
if scoreIn171>=73 and passed171==True:
    print("You can take 220")
else:
    print("You can't take 220")
##################################
num=35
if num>=0 and num<=10:
    print ("0")
elif num>10 and num<=20:
    print ("10")
elif num>20 and num<=30:
    print("20")
else:
    print("30")
############################
if num>=0 and num<=10:
    print("0")
elif num<=20:
    print("10")
elif num<=30:
    print("20")
else:
    print("30")
########################
score=105
if score>0 and score<100:
    if score<=59:
        grade="E"
        print (grade)
    elif score>=60 and score<70:
        grade="D"
        print(grade)
    elif score>=70 and score<80:
        grade="C"
        print (grade)
    elif score>=80 and score<90:
        grade="B"
        print (grade)
    elif score>=90 and score<100:
        grade="A"
else:
    grade="No grade"
    print(grade)
