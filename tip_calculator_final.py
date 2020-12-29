print("Welcome to the Tip Calculator")
bill_total = float(input("What was the bill total? $"))
print(bill_total)
tip = int(input("How much of a tip do you wish to leave? 10, 12, 15 \n"))

people_eating = int(input("How many people are splitting the bill?"))

percentage_tip = tip / 100
tip_amount = bill_total * percentage_tip
total_bill = tip_amount + bill_total

amount_to_pay = total_bill / people_eating
print(amount_to_pay)