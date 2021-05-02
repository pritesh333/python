
print("------------BMI-Calculator------------")

height = float(input("Enter your height in metres:"))
weight = float(input("Enter your weight in kilograms:"))

bmi = float(weight/(height*height))


print(f"Your Height is:{height} m")
print(f"Your Weight is:{weight} kg")

print(f"Your BMI is: {bmi}")

if(bmi<=18.5):
    print("Underweight")
elif(bmi<=24.9):
    print("Healthy")
elif(bmi<=29.9):
    print("Overweight")
else :
    print("Obese")

