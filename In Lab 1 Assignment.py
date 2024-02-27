#Asking User for Weight Input
weightinput = int(input("What is your weight (lbs)?"))
weightchange = 0.453592

#Doing Math for Weight in Kg
weightmetric = weightinput * weightchange

#Printing Math for Weight in Kg
print(f"Your weight in lbs is: {weightinput}")
print(f"Your weight in Kg is: {weightmetric}")

#Asking User for Height Input
heightinput = input("Enter your height in terms of feet (ft) and inches (in), separated by a comma: ' ")

#Seperating the Feet and Inches
height = heightinput.split(',')
feet = int(height[0])
inch = int(height[1])

#Doing Math for Height in M
heighttotal = feet * 12 + inch
heightchange = 0.0254
height = heighttotal * heightchange
print(f"Your height in M is: {height}")