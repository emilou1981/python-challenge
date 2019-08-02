#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text +
# file with the results.


import os
import csv
#declare starting value of total net profit
total_net_profit = 0
total_months = 0
#creat list for PL_differences
difference = []



# Path to collect data 
bank_csv = os.path.join("..", "RawData", "budget_data.csv")

#d
# Open and read csv
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
  
    # Read through each row of data after the header
    for row in csvreader:

# Define the function and have it accept the 'budget_data' as its sole parameter
        # def print_financials(BankBudget_data):

        Date = str(row[0])
        Profit_Loses = int(row[1])

        # Find the total number of months included in the dataset
        total_months = total_months + 1

        #the net total amount of "Profit/Losses" over the entire period
        total_net_profit = total_net_profit + Profit_Loses

        #define average to calculate average change

        # for i in range(1,len(d)):
        #     print(f'index {i}')
        #     previous = d[i-1]
        #     current = d[i]
        #     difference = current - previous
        #     print(f'current {current}, previous {previous}')
        #     print(f'difference {difference}')
 
                     
            # #The greatest increase in profits (date and amount) over the entire period
            # Incr_Profits = max[difference]

            # # #The greatest decrease in losses (date and amount) over the entire period
            # Decr_Profits = min[difference]
    
#     # Print out the financial analysis in terminal
    print("Financial Analysis")
    print("------------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_net_profit}')
    # print(f'Average Monthly Change: {Previous_Month_PL}')
    # print(f'Average Change: ${Average_Change}')
    # print(f'Greatest Increase in Profits: {Date} {Incr_Profits}')
    # print(f'Greatest Increase in Profits: {Date} {Decr_Profits}')

#export a text file with the results
# # Set variable for output file
# output_file = os.path.join("bank_Profit_Analysis_final.csv")

# #  Open the output file
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     writer.writerow(["Total Months", "Total Net Profit", "Average Change", "Max Profit Increase",
#                      "Min Profit Increase"])

#     # Write in zipped rows
#     writer.writerows(cleaned_csv)
