# Python-Challenge
Python HomeWork

To start the assignment first I imported the modules needed to complete the exercise, that being 'os' and 'csv'. Then the paths were created to read the csv as well as tell the code where to put the output text.
csvpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('analysis', 'output.txt')

Next the file was named and all used variables set to zero. Csv file was then opened and read as a dictionary to make it easier to manipulate. Rows were then idenitfied and calculations made for each file.

The output was then formatted and printed to a text file using the write function in csv. 



This was used in PyBank to format dollar amounts.
#https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string


This was used in PyPoll for formatting percent of votes received for each candidate.
#https://www.kite.com/python/answers/how-to-format-a-number-as-a-percentage-in-python#:~:text=Use%20str.,a%20number%20as%20a%20percentage&text=0%25%7D%22%20as%20str%20to%20format%20the%20number%20as%20a%20percentage.&text=To%20include%20a%20specific%20number,desired%20number%20of%20decimal%20places.


General references used
#https://www.geeksforgeeks.org/working-csv-files-python/
#https://stackoverflow.com/questions/13428318/reading-rows-from-a-csv-file-in-python
#https://docs.python.org/3/library/csv.html