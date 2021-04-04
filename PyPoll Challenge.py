# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
import os
import csv

# * You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#Row 1048576; Columns (3):  Voter_ID [0], County[1], Candidate[2]
filepath=r'C:\Users\Brad\Downloads\election_data.csv'

#search through csv file
with open(filepath)as csvfile:
    csvreader=csv.reader(csvfile)

#confirm file object
    print(csvreader)

#loop through rows
    for row in csvreader:
        print(row [0,1,2])



    #set variables 
    # x,y,z= "Voter_ID", "County", "Candidate"
    # ID=0
    # total_amounts=0

    # ID = []
    # total_amounts = []

    # for i in f:
    #     ID=ID+1
    #     total_amounts=total_amounts + int(Votes[1])
    #     ID.append(Votes[0])
    #     total_amounts.append(int(votes[1]))

    # print ("Election Results")
    # print(total_amounts)


#   * The total number of votes cast; sum of all rows

#   * A complete list of candidates who received votes; consolidated list (dedupe)

#   * The percentage of votes each candidate won; formula

#   * The total number of votes each candidate won; formula

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

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
  