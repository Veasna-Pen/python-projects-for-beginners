# Python Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds ? (K or L): ")

if unit.upper() == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight,1)} {unit}")
elif unit.upper() == "L":
    weight = weight / 2.205 
    unit = "Kgs."
    print(f"Your weight is {round(weight,1)} {unit}")
else:
    print(f"{unit} is not a valid unit")