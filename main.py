
print("Welcome to Tip Calculator.")
totalBill = float(input("What was the total bill? $"))
percentageOfTip = float(input("What percentage tip would you like to give? 10%, 12%, 15% or more than 15% ==>").replace("%",""))
#print(percentageOfTip)
numberOfPeople = float(input("How many people to split the bill? "))

tipValue = totalBill * (percentageOfTip / 100)
totalPayedValue = totalBill + tipValue
eachPersonShouldPay = round(totalPayedValue / numberOfPeople , 2)
eachPersonShouldPay = "{:.2f}".format(eachPersonShouldPay)
print(f"Each Person should pay: ${eachPersonShouldPay}")