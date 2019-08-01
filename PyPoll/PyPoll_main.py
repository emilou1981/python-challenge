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

# #A complete list of candidates who received votes
          
        # Candidate_List.append(Candidate_Name) 
        
#The percentage of votes each candidate won
        #print(d['Khan'])
        #num_votes = d[Candidate_Name]
        #for d[Candidate_Name] in d:
            #print(d[Candidate_Name])
        # #  #   Percentage_Won = (num_votes/Votes_Cast)*100
        # for key.value in d.[Candidate_Name(row[2]):
        # for key, value in d.items():
        # for k, v in d.items():
        # print(k, v)
            # for key, value in d.items():
                
            #     # print(k,v)

            #     Percentage_Won = (value/Votes_Cast)*100
#finding winner of election
for key in d.keys():
    if d[key] > winningTotal:
        winningTotal = d[key]
        Winner = key
# print(winningTotal)
# print(Winner)

#calculate candidate percentages
for key, Votes in d.items():
    Win_Percent[key] = (Votes/Votes_Cast)*100
    # print(Win_Percent[key])   
    

    # if d.[key] > winningTotal:
    #     winningTotal = d[key]
    #     Winner = key
  

# for key in d.keys():
#     if d
#     Percentage_Won = (float(key)/Votes_Cast)*100
        
# for name in Candidate_Votes:


#The total number of votes each candidate won



#The winner of the election based on popular vote.     

       

    # Unique_Candidate_List = set(Candidate_List)
#     # Print out the results


print("Election Results")
print("------------------------------------")
print(f'Total Votes: {Votes_Cast}')
print("------------------------------------")
for key in d.keys():
    print(f'{key}: {Win_Percent[key]} ({d[key]})')
print("------------------------------------")   
print(f'Winner: {Winner}')
print("------------------------------------")   
# print(f'List of Candidates: {d}')
    # for d[Candidate_Name] in d:
    #         #print(d[Candidate_Name])
    #     print(int(d[Candidate_Name]))
      #Percentage_Won = (int(d[Candidate_Name])/Votes_Cast)*100
    # print(int(d[Candidate_Name]))
    # print({Percentage_Won})