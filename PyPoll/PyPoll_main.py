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
Candidate_Votes = []
Candidate_Votes = 0
Candidate_List = []

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

        # Candidate_Votes[Candidate_Name]+=1

# #A complete list of candidates who received votes
          
        Candidate_List.append(Candidate_Name) 
        
#The percentage of votes each candidate won

# for name in Candidate_Votes:
#     print(f'{Candidate_Name}: {Candidate_Votes[name]}(, ({Votes_Cast} / {Candidate_Votes[name]}),)' )


#The total number of votes each candidate won



#The winner of the election based on popular vote.     

       

    Unique_Candidate_List = set(Candidate_List)
#     # Print out the results
    print("Election Results")
    print("------------------------------------")
    print(f'Total Votes: {Votes_Cast}')
    print("------------------------------------")
    print(f'List of Candidates: {Unique_Candidate_List}')