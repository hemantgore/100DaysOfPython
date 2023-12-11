# 1st input: enter height in meters e.g: 1.65
height = input("Enter height in meter\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Enter weight in Kg.\n")

# Write your code below this line 👇
bmi = float(weight) / (float(height)*float(height))
print(int(bmi))
