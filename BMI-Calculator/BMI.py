#BMI Calculator
print("Welcome to BMI Calculator")
h = float(input("Enter the height in Meters :-"))
w = float(input("Enter the weight in Kilograms :-"))
bmi = round((w/h**2),3)
print("Your BMI = ", bmi)
if bmi <= 18.5:
    print("You are UnderWeight")
elif 18.5 < bmi <= 24.9:
    print("Your Weight is normal")
elif 25 < bmi <= 29.29:
    print("You are Overweight")
else:
    print("you are Obese")