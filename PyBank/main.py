# set libraries
import os
import csv

# initialize variables - set to zero
total_months = 0
total_amount = 0
greatest_increase = 0
greatest_decrease = 0
row_counter = 0
prev_row = 0
monthly_change = []

# path for csv resource File
budget_csv = os.path.join('Resources', 'budget_data.csv')

# open file - set delimited
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header and store in variable
    csv_header = next(csvreader)

    # analysis loop - month count and profit tracking
    for row in csvreader:
        total_months += 1
        total_amount += int(row[1])

        # track change in profit/loss
        if row_counter != 0:
            profit_change = int(row[1]) - prev_row
            monthly_change.append(profit_change)
            prev_row = int(row[1])

            # greatest increase
            if profit_change > greatest_increase:
                greatest_increase = profit_change
                gi_month = row[0]

            # greatest decrease   
            if profit_change < greatest_decrease:
                greatest_decrease = profit_change
                gd_month = row[0]
        # handle first row
        else:
            prev_row = int(row[1])
            row_counter += 1

# determine the average profit/loss over the provided timeframe
average_change = sum(monthly_change) / len(monthly_change)

# build output f-string
output_string = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_amount}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {gi_month} (${greatest_increase})
Greatest Decrease in Profits: {gd_month} (${greatest_decrease})
"""

# print output info to the terminal
print(output_string)

# write out to text file
with open("analysis/PyBank_Analysis.txt", "w") as csvfile:
    csvfile.write(output_string) 



