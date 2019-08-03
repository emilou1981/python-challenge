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
#declare starting values
total_net_profit = 0
total_months = 0
#creat list for PL_differences
difference = []
diff_List = []
PL_List = []
Date_List = []
Average_Change = 0
Aver_with_Date =[]
Max = []
Min = []

# Path to collect data 
bank_csv = os.path.join("..", "RawData", "budget_data.csv")

# Open and read csv
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
  
    # Read through each row of data after the header
    for row in csvreader:

        # Define a title for the rows of data
        Date = str(row[0])
        Profit_Loses = int(row[1])

        #create new lists for PL and Date to create the comparision of two values (x and x-1)
        PL_List.append(Profit_Loses)
        Date_List.append(Date)

        # Find the total number of months included in the dataset
        total_months = total_months + 1

        #the net total amount of "Profit/Losses" over the entire period
        total_net_profit = total_net_profit + Profit_Loses

# remove the first date to zip with comparision as row 1 PL is none
Date_List.pop(0)
    
# compare the Profit lose values x minus (x-1) to get monthly change and add value to new list (diff_List):
for i in range(1,len(PL_List)):
    # print(f'index {i}')
    previous = PL_List[i-1]
    current = PL_List[i]
    difference = current - previous
    diff_List.append(difference)
    # print(f'current {current}, previous {previous}')
    # print(f'difference {difference}')

#calcuate average change of the monthly changes
Average_Change = round(sum(diff_List)/(total_months-1),2)
                     
#Zip together the updated date list with the removed 1st date and the month changes into a new list
Aver_with_Date = zip(Date_List, diff_List)
for i in Aver_with_Date:
    for j in i:
        if j == max(diff_List):
            Max = i
             # print(Max)
        if j == min(diff_List):
            Min = i
            # print(i)

    
# Print out the financial analysis in terminal
print("Financial Analysis")
print("------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_net_profit}')
print(f'Average Change: ${Average_Change}')
print(f'Greatest Increase in Profits (Date / $): {Max}')
print(f'Greatest Decrease in Profits (Date / $): {Min}')

# export a text file with the results
# Set variable for output file
output_file = os.path.join("bank_Profit_Analysis_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Total Months", "Total Net Profit ($)", "Average Change ($)", "Max Profit Increase (Date, $)", "Min Profit Decrease (Date, $)"])
    writer.writerow([total_months, total_net_profit, Average_Change, Max, Min])

