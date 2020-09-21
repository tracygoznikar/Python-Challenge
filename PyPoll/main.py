#import modules
import os
import csv

#write file path
csvpath = os.path.join('Resources', 'election_data.csv')
outpath = os.path.join('analysis', 'output.txt')

#name file
file_name = 'election_data.csv'

#set variables and set to 0
total_votes = 0
candidate_list = 0
percent_votes_won = 0
totalnum_votes_won = 0
winner = 0

#initializing rows
Voter_ID = []
County = []
Candidate = []


#open and read file csv
with open(csvpath, 'r') as csvfile:
    # CSV reader and set as dict
    csvreader = csv.DictReader(csvfile)
   # Reads each row of the dict
    for row in csvreader:
        # read colums and make integer
    break