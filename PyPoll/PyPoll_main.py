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
Votes = []
Votes = 0
# Candidate_List = []
Received_Votes = []
Percentage_Won = []
Win_Percent = {}
d = {}
num_votes = 0
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

# Define the function and have it accept the 'election_data' as its sole parameter
        Voter_ID = int(row[0])
        County = str(row[1])
        Candidate_Name = str(row[2])

#The total number of votes cast
        Votes_Cast = Votes_Cast + 1
        
# create dictionary and count candidate votes
        
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
    

print("Election Results")
print("------------------------------------")
print(f'Total Votes: {Votes_Cast}')
print("------------------------------------")
for key in d.keys():
    print(f'{key}: {Win_Percent[key]}% ({d[key]})')
print("------------------------------------")   
print(f'Winner: {Winner}')
print("------------------------------------")   
