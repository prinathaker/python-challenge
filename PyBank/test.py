import os
import csv
import formatter
total = 0
nettotal = 0

# dictionary for greatest increase and decrease
great_inc = {"month": "", "value":0}
great_dec = {"month": "", "value" : 0}

monthly_change = []
previous_value = 0
profit_change = 0

# specify input file name and path
currt_dir = os.getcwd()
read_path = './Resources'
budget_csv = os.path.join(currt_dir,read_path,'budget_data.csv')

# specify output file name and path
#save_path = '/Users/Pulast/data boot camp/projects/python-challenge/pybank/Analysis'
save_path = './Analysis'
file_name = "budget_analysis.txt"
OutputFileName = os.path.join(currt_dir,save_path,file_name)
print(OutputFileName)

with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    data = list(csvreader)
    
    # Total Months in the file
    row_count = len(data)
    
# Read each row of data after the header
    for row in data:

        #total months
        total = total + int(row[1])

         #Find greatest increase and decrease
        if great_inc["value"] < int(row[1]):
            great_inc["month"] = row[1]
            great_inc["value"] = int(row[1])
        if great_dec["value"] > int(row[1]):
            great_dec["month"] = row[1]
            great_dec["value"] = int(row[1])

        #count average changes for entire period
        profit_change = int(row[1]) - previous_value
        monthly_change.append(profit_change)
        previous_value = int(row[1])
        
    #calculate average change
    average_change = sum(monthly_change) / row_count
        
result = (
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {row_count}\n"
    f"Total: ${total}\n"
    f"Average Change: ${round(average_change,2)}\n"
    f"Greatest Increase in Profits: {great_inc['month']}  (${great_inc['value']})\n"
    f"Greatest Decrease in Profits: {great_dec['month']}  (${great_dec['value']})\n"
)

#print results on terminal
print(result)

#Open Outputfile and add budge analysis results
with open(OutputFileName, "w+") as txt_file:
    txt_file.write(result)
    txt_file.close()