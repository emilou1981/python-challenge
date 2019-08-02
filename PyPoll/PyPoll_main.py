#Your task is to create a Python script that analyzes the votes and calculates each of the following:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote.
    #In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import os
import csv

#declare starting values
Votes_Cast = 0

#dictionary to calc winning percent
Win_Percent = {}

#dictionary to compile total votes received by candidates
d = {}

#varibles to determining winner based on totals
winningTotal = 0
Winner = ""

# Path to collect data 
election_csv = os.path.join("..", "RawData", "election_data.csv")

# Open and read csv
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
  
    # Read through each row of data after the header
    for row in csvreader:

        # Define the candidate name from CSV file
        Candidate_Name = str(row[2])

        #Count the total number of votes cast
        Votes_Cast = Votes_Cast + 1
        
        # create dictionary and count candidate votes received   
        if Candidate_Name in d:
            d[Candidate_Name] = d[Candidate_Name] + 1
        else:
            d[Candidate_Name] = 1

#Determine winner of election
for key in d.keys():
    if d[key] > winningTotal:
        winningTotal = d[key]
        Winner = key
# print(winningTotal)
# print(Winner)

#calculate candidate percentages
for key, Votes in d.items():
    Win_Percent[key] = round((Votes/Votes_Cast)*100,3)
    # print(Win_Percent[key])   
   
    
#print out data for output for terminal
print("Election Results")
print("------------------------------------")
print(f'Total Votes: {Votes_Cast}')
print("------------------------------------")
#write out print string referencing the keys from d and win_percent dictionaries
for key in d.keys():
    print(f'{key}: {Win_Percent[key]}% ({d[key]})')
print("------------------------------------")   
print(f'Winner: {Winner}')
print("------------------------------------")   

# export a text file with the results
# Set variable for output file
output_file = os.path.join("Polling_Results_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["FINAL ELECTION RESULTS"])
    writer.writerow(["==================================================================================="])
    writer.writerow(["Winner:"])
    writer.writerow([Winner])
    writer.writerow(["==================================================================================="])
    writer.writerow(["Total Votes Cast"])
    writer.writerow([Votes_Cast])
    writer.writerow(["==================================================================================="])
    writer.writerow(["Candidate"])
    writer.writerow([key]) 
    writer.writerow(["Percentage of Votes"])
    writer.writerow([{Win_Percent[key]}])
    writer.writerow(["Votes Received"])
    writer.writerow([{d[key]}])
   
