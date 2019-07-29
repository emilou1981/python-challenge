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
            #he net total amount of "Profit/Losses" over the entire period
        
            total_net_profit = total_net_profit + Profit_Loses
            #define average to calculate average change
            #     Average_Change = 
            # #The greatest increase in profits (date and amount) over the entire period
            #     Incr_Profits = 
            # #The greatest decrease in losses (date and amount) over the entire period
            #     Decr_Profits = 

#     # Print out the financial analysis
    print("Financial Analysis")
    print("------------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: {total_net_profit}')
    # print(f'Greatest Increase in Profits: {Date} {Incr_Profits}')
    # print(f'Greatest Increase in Profits: {Date} {Decr_Profits}')

# # Read in the CSV file
# with open(wrestling_csv, 'r') as csvfile:

#     # Split the data on commas
#     csvreader = csv.reader(csvfile, delimiter=',')

#     # Prompt the user for what wrestler they would like to search for
#     name_to_check = input("What wrestler do you want to look for? ")

#     # Loop through the data
#     for row in csvreader:

#         # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
#         if(name_to_check == row[0]):
#             print_percentages(row)

# # Zip lists together
# cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# # Set variable for output file
# output_file = os.path.join("web_final.csv")

# #  Open the output file
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
#                      "Percent of Reviews", "Length of Course"])

#     # Write in zipped rows
#     writer.writerows(cleaned_csv)