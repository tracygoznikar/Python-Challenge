#import modules
import os
import csv

budgetdate = 0
total_months = 0
profit_loss = 0
increase_profit = 0
decrease_profit = 0
average_profit = 0

#write file path
csvpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('analysis', 'output.txt')

# identify values
with open(csvpath) as csvfile:
    # CSV reader and specify delimiter, print
    #csvreader = csv.DictReader(csvfile, delimiter=',')
    csvwriter = csv.writer(budgetdate, profit_loss, delimiter=',')
    

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvwriter)
    print(f"CSV Header: {csv_header}")


    # Read each row of data after the header
    for row in csvwriter:
            #budgetdate.append(row[0])
        #print(budgetdate)
        #print(row[0] + "," + row[1])
        #print(row)
        #total_months = len(budgetdate)
        #print(total_months)
            total_months = total_months +1
            print(total_months)
            break
        #total number of months in the dataset


#the net total amount of "Profit/Losses" over the entire period
    

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


#the greatest increase in profits (date and amount) over the entire period


#formated_average = "{:.2f}".format(average


#the greatest decrease in losses (date and amount) over the entire 