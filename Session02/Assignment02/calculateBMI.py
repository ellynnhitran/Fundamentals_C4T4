heightcm = float(input("What is your height?(cm) "))
height = (heightcm) / 100
mass = float(input("What is your weight?(kg) "))
BMI = (mass) / (height*height)

if BMI < 16:
    print("You are severely underweight")
elif 16 < BMI < 18.5:
    print("You are underweight")
elif 18.5 < BMI < 25:
    print("You are normal")
elif 25 < BMI < 30:
    print("You are overweight")
elif BMI > 30:
    print("You are obese")

