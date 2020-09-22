#import modules
import os
import csv

#write file path
csvpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('analysis', 'output.txt')

#name file
file_name = 'budget_data.csv'

#set variables and set to 0
number_months = 0
net_profit_loss = 0
avg_profit_loss = 0
max_profit = 0
loss_profit = 0

#initializing rows
budget_row = []
Profit/Losses = []

#open and read file csv
with open(csvpath, 'r') as csvfile:
    # CSV reader and set as dict
    csvreader = csv.DictReader(csvfile)
   # Reads each row of the dict
    for row in csvreader:
        # read colums and make integer
        budget_row = int(row["Profit/Losses"]) 
        net_profit_loss += int(row["Profit/Losses"])
        # compare rows to find max amount
        if max_profit == 0 or max_profit < budget_row:
            max_profit = int(budget_row)
        # compare rows to find min
        if loss_profit == 0 or loss_profit > budget_row:
            loss_profit = int(budget_row)   
    
    # Creates variable for counting the number of lines, minus the header row   
    number_months = csvreader.line_num - 1
    
    # Format values using "${:.2f}"
    avg_profit_loss = "${:,.2f}".format(net_profit_loss/number_months)
    net_profit_loss = "${:,.2f}".format(net_profit_loss)
    max_profit = "${:,.2f}".format(max_profit)
    loss_profit = "${:,.2f}".format(loss_profit)


  # Prints to terminal
    print(f"CSV Path: {csvpath}") 
    print(f"Analysis Path: {outpath}")
    print(f" ")
    print(f"Budget Analysis of {file_name}")
    print(f"Total Number of Months: {number_months}")
    print(f"Net PL: {net_profit_loss}")
    print(f"Average PL: {avg_profit_loss}")
    print(f"Greatest Increase: {max_profit}")
    print(f"Greatest Decrease: {loss_profit}")

with open(outpath, 'w')
   csvwriter = csv.writer(csvfile, delimiter=' ')
    # Read each row of data after the header
    for row in csvwriter:        

    # Print out the ouput
        print("Financial Analysis")
        print("------------------")
        print(f"Total Months: {str(number_months)}")
        print(f"Total: {str(net_profit_loss)}")
        print(f"Average Change: {str(avg_profit_loss)}")
        print(f"Greatest Increase of Profits: {str(max_profit)}")
        print(f"Greatest Decrease in Profits {str(loss_profit)}")


#format = "${:.2f}"


#resources used
#https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string
#https://docs.python.org/3/library/csv.html
#https://www.geeksforgeeks.org/working-csv-files-python/
#https://stackoverflow.com/questions/13428318/reading-rows-from-a-csv-file-in-python





# old code below- non-working


# identify values
#with open(csvpath) as csvfile:
    # CSV reader and specify delimiter, print
    #csvreader = csv.DictReader(csvfile, delimiter=',')
 #   csvwriter = csv.writer(budgetdate, profit_loss, delimiter=',')
    # Read the header row first (skip this step if there is now header)
  #  csv_header = next(csvwriter)

    # Read each row of data after the header
   # for row in csvwriter:        

    # Print out the ouput
    #    print("Financial Analysis")
     #   print("------------------")
      #  print(f"Total Months: {str(total_months)}")
       # print(f"Total: {str(profit_loss_total)}")
       # print(f"Average Change: {str(average_profit)}")
       # print(f"Greatest Increase of Profits: {str(increase_profit)}")
       # print(f"Greatest Decrease in Profits {str(decrease_profit)}")

    

#the average of the changes in "Profit/Losses" over the entire period
#with open(csvpath,newline='') as csvfile:
    #csvreader = csv.reader(csvfile,delimiter=",")
    # csvreader2 = csv.reader(csvfile,delimiter=",")
    #csv_header = next(csvreader)
# # print(csv_header)

    #for row in csvreader:
     #   profit_loss.append(row[1])

     
    #print(profit_loss[0])
    #print(profit_loss[85])
    #avgchange=(int(profit_loss[85])-int(profit_loss[0]))/85
    #print(average_profit)
