print("Welcome tip calculator")
bill = float(input("What is total bill?$"))

tip = int(input("What % tip would you like to give? 10, 12, or 15\n"))

ppl = int(input("How many people to split the  bill\n"))

tip_per = tip / 100
tip_amt = bill * tip_per
total_bill = bill + tip_amt
bill_per_person = round((total_bill / ppl), 2)
print(f"Each person should pay: ${bill_per_person}.")
