print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_split = int(input("how many people to split the bill? "))

#Get total after giving percentage tip
new_total_bill = round(total_bill + (float(percent_tip / 100) * total_bill),2)

#Calculate how much per person
split_per_person = round(float(new_total_bill / people_split),2)

#Print how much each person should pay
print(f"Each person should pay ${split_per_person}.")
