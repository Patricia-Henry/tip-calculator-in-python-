print("Welcome to the Tip Calculator")
bill_total = float(input("What was the bill total? $"))
people_eating = int(input("How many people are splitting the bill?"))
tip = int(input("How much of a tip do you wish to leave? 10, 12, 15 \n"))
percentage_tip = tip / 100
tip_amount = bill_total / percentage_tip
amount_to_pay = bill_total / people_eating
print(amount_to_pay)