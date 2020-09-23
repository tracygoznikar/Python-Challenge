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
winner = str
kvote = 0
cvote = 0
lvote = 0
tvote = 0
kpercent = 0
cpercent = 0
lpercent = 0
tpercent = 0


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
  # percent of votes each candidate won
    #(kvote / total_votes) * 100 = kpercent
    #(cvote / total_votes) * 100 = cpercent
    #(lvote / total_votes) * 100 = lpercent
   # (tvote / total_votes) * 100 = tpercent


  #total number of votes cast
total_votes = csvreader.line_num - 1

# percent of votes each candidate won
kpercent = "{:.3%}".format(kvote/total_votes)
cpercent = "{:.3%}".format(cvote/total_votes)
lpercent = "{:.3%}".format(lvote/total_votes)
tpercent = "{:.3%}".format(tvote/total_votes)
  #winner of election based on votes

if kpercent > "{:.3%}".format(50):
        Candidate = winner
#if cpercent > 50:
#        Candidate = winner
#if lpercent > 50:
#        Candidate = winner
#if tpercent > 50:
#        Candidate = winner

with open(outpath, 'w') as text_file:   
    # Print out the ouput
    print("Election Results", file=text_file)
    print("------------------", file=text_file)
    print(f"Total Votes: {str(total_votes)}", file=text_file)
    print("------------------", file=text_file)
    print(f"Khan: {str(kpercent)}  {str(kvote)}", file=text_file)
    print(f"Correy: {str(cpercent)}  {str(cvote)}", file=text_file)
    print(f"Li: {str(lpercent)}  {str(lvote)}", file=text_file)
    print(f"O'Tooley: {str(tpercent)}  {str(tvote)}", file=text_file)
    print("------------------", file=text_file)
    print(f"Winner: {str(winner)}", file=text_file)
    print("------------------", file=text_file)