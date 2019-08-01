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
Month_Change = 0
Average_Change = []
Average_Change = 0
Previous_Month_PL= {}
Previous_Date = ""
Prior_Month_Change = []
Profit_Loses = []





# Path to collect data 
bank_csv = os.path.join("..", "RawData", "budget_data.csv")

#loop through data first time to establish list for prior profit/loss
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    skip_2nd = next(csvfile)
  
    # Read through each row of data after the header
    for row in csvreader:
# Define the function and have it accept the 'budget_data' as its sole parameter
        # def print_financials(BankBudget_data):

        Previous_Date = str(row[0])
        Previous_Month_PL = int(row[1])
        # print(f'{Previous_Date} : {Previous_Month_PL}')


#-------------------------------------------------------------------
# Second loop
# Path to collect data 
bank_csv = os.path.join("..", "RawData", "budget_data.csv")
# Open and read csv
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
  
    # Read through each row of data after the header
    for row in csvreader:

# Define the function and have it accept the 'budget_data' as its sole parameter
    

        Date = str(row[0])
        Profit_Loses = int(row[1])

        # Find the total number of months included in the dataset
        total_months = total_months + 1

        #the net total amount of "Profit/Losses" over the entire period
        total_net_profit = total_net_profit + Profit_Loses

#The average of the changes in "Profit/Losses" over the entire period
       
        # Prior_Month_Change = Profit_Loses
        Prior_Month_Change = ((Previous_Month_PL - Profit_Loses))

        print(f'Prior Month Change: {Prior_Month_Change}')

# Average_Change = sum(Prior_Month_Change)/(total_months - 1)


           
            
            # Average_Change = round((total_net_profit / total_months),2)
            # #The greatest increase in profits (date and amount) over the entire period
            #     Incr_Profits = 
            # #The greatest decrease in losses (date and amount) over the entire period
            #     Decr_Profits = 


#     # Print out the financial analysis
print("Financial Analysis")
print("------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_net_profit}')
print(f'Average Change: {Prior_Month_Change}')
    # print(f'Average Monthly Change: {Previous_Month_PL}')
    # print(f'Average Change: ${Average_Change}')
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