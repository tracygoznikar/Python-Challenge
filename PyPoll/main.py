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
kvote = 0
cvote = 0
lvote = 0
tvote = 0

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
        Voter_ID = int(row["Voter ID"]) 
        County = str(row["County"])
        Candidate = str(row["Candidate"])
      # total number of votes each candidate won    
        if Candidate == "Khan":
            kvote = kvote + 1
        if Candidate == "Correy":
            cvote = cvote + 1
        if Candidate == "Li":
            lvote = lvote + 1
        if Candidate == "O'Tooley":
            tvote = tvote + 1
  #total number of votes cast
total_votes = csvreader.line_num - 1
  # percent of votes each candidate won

  #winner of election based on votes

with open(outpath, 'w') as text_file:   
    # Print out the ouput
    print("Election Results", file=text_file)
    print("------------------", file=text_file)
    print(f"Total Votes: {str(total_votes)}", file=text_file)
    print("------------------", file=text_file)
    print(f"Khan: {str(kvote)}", file=text_file)
  #  print(f"Average Change: {str(avg_profit_loss)}", file=text_file)
   # print(f"Greatest Increase of Profits: {str(max_profit)}", file=text_file)
    #print(f"Greatest Decrease in Profits {str(loss_profit)}", file=text_file)