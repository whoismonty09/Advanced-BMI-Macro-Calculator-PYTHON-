print("BMI and Macro Calculator developed by Monty")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))
age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ").lower()

if gender == "male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

def macros(calories):
    protein = weight * 1.6
    carbs = (calories * 0.5) / 4
    fat = (calories * 0.25) / 9
    fiber = 30
    return int(protein), int(carbs), int(fat), fiber

maintain = bmr
mild_loss = bmr - 250
loss = bmr - 500
extreme_loss = bmr - 1000

mild_gain = bmr + 250
gain = bmr + 500
fast_gain = bmr + 1000

plans = {
    "Maintain Weight": maintain,
    "Mild Weight Loss (0.25 kg/week)": mild_loss,
    "Weight Loss (0.5 kg/week)": loss,
    "Extreme Weight Loss (1 kg/week)": extreme_loss,
    "Mild Weight Gain (0.25 kg/week)": mild_gain,
    "Weight Gain (0.5 kg/week)": gain,
    "Fast Weight Gain (1 kg/week)": fast_gain
}

print("\n--- Calories and Macros Plan ---\n")

for plan, cal in plans.items():
    protein, carbs, fat, fiber = macros(cal)
    print(plan)
    print("Calories/day:", int(cal))
    print("Protein (g):", protein)
    print("Carbs (g):", carbs)
    print("Fat (g):", fat)
    print("Fiber (g):", fiber)
    print()
