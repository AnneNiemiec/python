# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
import os
import csv

# * You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#Row 1048576; Columns (3):  Voter_ID [0], County[1], Candidate[2]
filepath=r'C:\Users\Brad\Desktop\03-Python\PyPoll\Resources\election_data.csv'

#   * The total number of votes cast; sum of all rows
#set variables 
Voter_ID=0
total_votes=0
election_results=0
Winner=""

#The net total amounts over the entire period
voter_tally = []
candidate_name=[]
votes_per_candidate={}
percent_won=[]

#   * A complete list of candidates who received votes; consolidated list (dedupe)
#search through csv file
with open(filepath)as csvfile:
    csvreader=csv.reader(csvfile)

    #read header
    header=next(csvreader)

#loop through rows
    for row in csvreader:
        voter_tally.append(row[2])
        
        #Look for list of unique candidates
        if row[2] not in votes_per_candidate:
            votes_per_candidate[row[2]]= 1      # of votes thus far
        elif row[2] in votes_per_candidate:
            votes_per_candidate[row[2]] +=1 
        total_votes=total_votes+1
        
text_file=(
f"Election Results\n ===============\n"
f"Total Votes: {total_votes}\n ===============\n"
)

# of votes won by candidate
print (votes_per_candidate)
for candidate in votes_per_candidate:
    percent_won= (votes_per_candidate[candidate]/total_votes) *100
    text_file=text_file+ f"{candidate} :{percent_won:.2f}% ({votes_per_candidate[candidate]})\n"
        
Winner=max(votes_per_candidate,key=votes_per_candidate.get)
text_file=text_file+(
    f"==============\n"
    f"Winner: {Winner}")
print (text_file)


#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan

 # of votes won by percentage 
with open("PyPoll\Resources\PyPoll_ATN.txt","w") as csvfile:

    csvfile.write(text_file)
