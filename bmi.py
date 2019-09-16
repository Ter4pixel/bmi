print("Body Mass Index Calculator by Sean Slatkavitz")
weight = int(input("Body weight (lbs): "))
height = int(input("Height (feet): "))
heightinches = int(input("Height (inches) (Example: if you put 6 in for feet and you are 6 foot 2 then enter 2 here): "))
totalheight = height * 12 + heightinches
print(totalheight)

formula = (weight / totalheight / totalheight) * 703
print("Your BMI is " + str(formula) + ".")
