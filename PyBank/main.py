#import modules
import os
import csv

#write file path
csvpath = os.path.join('..', r'Resources', r'budget_data.csv')

#open file
with open(csvpath) as csvfile:

    # CSV reader and specify delimiter, print
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

#script that analyzes the following
#total number of months included in the dataset


#the net total amount of "Profit/Losses" over the entire period
#the average of the changes in "Profit/Losses" over the entire period
#the greatest increase in profits (date and amount) over the entire period
#the greatest decrease in losses (date and amount) over the entire period
