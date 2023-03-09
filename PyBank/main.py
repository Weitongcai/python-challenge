import os
import csv

budget_path = os.path.join("Resources", "budget_data.csv")

totalnum_month = 0
total_profit = 0
previouse_profit = 0
profit_change = 0
months = []
profit_changes = []


with open(budget_path, 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    header_row = next(reader)

    for row in reader : 
        #Total number of months included in the dataset
        totalnum_month += 1
        # Net total anount of "Profit/Losses" over the entire period
        total_profit += int(row[1])
        #Changes in "Profit/Losses" over the entire period
        if totalnum_month > 1 :
           profit_change = int(row[1]) - previouse_profit
           profit_changes.append(profit_change)
           months.append(row[0])
        
        previouse_profit = int(row[1])


# average change in "Profit/Losses" over the entire period
average_change = round(sum(profit_changes)/len(profit_changes),2)

#greatest increase and decrease in profit
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)
greatest_increase_date = months[profit_changes.index(greatest_increase)]
greatest_decrease_date = months[profit_changes.index(greatest_decrease)]

# Print out
print("Financial Analysis")
print("--------------------------------")
print(f"Total Month: {totalnum_month}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")