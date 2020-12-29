#Ask for total bill
print("What was the total bill?")
total_bill = input()

#Ask for how many people are splitting the bill
print("How many people to split the bill?")
people_dining = input ()

#(total bill / people dining) * percent tip
#In this case total bill is 150.00 divided by 5 people times 12 percent tip

total = (float(total_bill) / int(people_dining)) * 1.12

print(total)





