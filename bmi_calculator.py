# This is day 1 of me built my project

"""
BMI Calculator
This Python script calculates Body Mass Index (BMI) based on a person's height and weight. It then interprets the BMI to provide a classification ranging from underweight to clinically obese.
"""
#BMI = BB / (TB(cm) ** 2) * 10000

#THE TITLE OF CALCULAOTR
print("THIS IS BMI CALCULATOR")

#user input thier height and weight
height =  int(input("Input your height in kg (e.g 190) : "))
weight = int(input("Inpur your wight in cm (e.g 80) : "))

#formula of bmi calculator
bmi_result = float(weight / (height ** 2 )) * 10000

#bmi's category
if bmi_result < 18.5:
    categories = "Under Weight"
elif bmi_result < 25:
    categories = " Healthy Weight"
elif bmi_result < 30:
    categories = "Overweight"
elif bmi_result < 40:
    categories = "Obesity"
else:
    categories = "Severe Obesity"

#show output for user
print(f"Your BMI is {bmi_result:.2f}.")
print(f"You categorized by {categories}.")