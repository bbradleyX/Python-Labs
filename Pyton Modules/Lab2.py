#Name:Bria Bradley
#Date: 9/26/17
#Purpose: To calculate the total area of a house with dimensions from user input
width=float(input("Enter width of house: "))
#Check: print(width)
length=float(input("Enter length of house: "))
#Check: print(length)
height=float(input("Enter height of house: "))
#Check: print(height)
gableHeight=float(input("Enter gable height of house: "))
#Check: print(gableHeight)
#Front/Back Calculation: 2(Length x Height)
front=(length*height)
back=front
print("front,back:",front,back)
#Side Calculation: Width x Height
side1=(width*height)
side2=side1
print("side1,side2:",side1,side2)
#Gable Calulation:(1/2)Width x GableHeight
gable1=((width*gableHeight)/2)
gable2=gable1
print("gable1,gable2:",gable1,gable2)
totalArea=((2*front)+(2*side1)+(2*gable1))
print("Total area of house:",float(totalArea))
totalPaint=(totalArea/400)
print("Total gallons of paint needed:",int(totalPaint)+1)
