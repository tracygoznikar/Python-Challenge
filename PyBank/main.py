#import modules
import os
import csv
import statistics

budgetdate = 0
total_months = 0
profit_loss_total = 0
increase_profit = 0
decrease_profit = 0
average_profit = 0

#write file path
csvpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('analysis', 'output.txt')


def print_percentages(budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    date = int(budget_data[0])
    profit_loss = int(budget_data[1])

    # Total months 
    total_months = 

    # the net total amount of "Profit/Losses" over the entire period
    win_percent = (wins / total_matches) * 100

    # the average of the changes in "Profit/Losses" over the entire period
    loss_percent = (losses / total_matches) * 100

    # the greatest increase in profits (date and amount) over the entire period
    draw_percent = (draws / total_matches) * 100

    #the greatest decrease in losses (date and amount) over the entire period





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
        

    # Print out the ouput
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {str(total_months)")
    print(f"Total: {str(profit_loss_total)}")
    print(f"Average Change: {str(average_profit)}")
    print(f"Greatest Increase of Profits: {str(increase_profit)}")
    print(f"Greatest Decrease in Profits {str(decrease_profit)}")

    

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