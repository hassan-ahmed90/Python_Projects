

print("Welcome to Tip Calculator !")
total_bill=int(input("What was your total bill ?\n"))
tip=int(input("How much tip you want to give? 10 12 15?\n"))
people=int(input("How many people to split the bill?\n"))
calculated_tip=(total_bill/100)*tip
calculated_bill=(total_bill+calculated_tip)/people
print(f"Your bill for each person is {calculated_bill}")