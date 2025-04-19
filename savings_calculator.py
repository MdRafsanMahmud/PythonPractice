# Savings Calculator Starter File

# Task 1: Setting Up Variables
# Create variables for monthly savings here
month1 = 5000
month2 = 6000
month3 = 8000

# Task 2: Calculating Total Savings
# Calculate total savings here
total_savings = month1 + month2 + month3

# Task 3: Calculating Average Savings
# Calculate average savings here
num_month = 3
average_savings = round(total_savings / num_month)

# Task 4: Formatting and Printing Results
# Print the formatted results here
print("Total Savings: $" + str(total_savings))
print("Average Savings: $" + str(average_savings))

# Bonus Challenges:

# 1. Modify the program to handle 4 months of savings
print("\nModify the program to handle 4 months of savings:")
month4 = '7000'

total_savings = month1 + month2 + month3 + int(month4)
num_month = 4
average_savings = round(total_savings / num_month)

month1_percentage = (month1 / total_savings) * 100
month2_percentage = (month2 / total_savings) * 100
month3_percentage = (month3 / total_savings) * 100
month4_percentage = (int(month4) / total_savings) * 100

print("Month 1 Contribution: " + str(round(month1_percentage, 2)) + "%")
print("Month 2 Contribution: " + str(round(month2_percentage, 2)) + "%")
print("Month 3 Contribution: " + str(round(month3_percentage, 2)) + "%")
print("Month 4 Contribution: " + str(round(month4_percentage, 2)) + "%")
# 2. Round the average savings to the nearest whole dollar
print("\nRound the average savings to the nearest whole dollar:")
average_savings = round(average_savings)
print("Average Savings: $" + str(average_savings))

# 3. Calculate what persentage each month's savings contribute to the total
print("\nCalculate what persentage each month's savings contribute to the total:")
month1_percentage = (int(month1) / total_savings) * 100
month2_percentage = (int(month2) / total_savings) * 100
month3_percentage = (int(month3) / total_savings) * 100
month4_percentage = (int(month4) / total_savings) * 100

print("Month 1 Contribution: " + str(round(month1_percentage, 2)) + "%")
print("Month 2 Contribution: " + str(round(month2_percentage, 2)) + "%")
print("Month 3 Contribution: " + str(round(month3_percentage, 2)) + "%")
print("Month 4 Contribution: " + str(round(month4_percentage, 2)) + "%")


# Your bonus code here