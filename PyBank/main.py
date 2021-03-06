import os
import csv

# dictionary for greatest increase and decrease
great_inc = {"month": "", "value":0}
great_dec = {"month": "", "value" : 0}

#lists for various calculations
monthly_change = []
month_count = []
profit = []
chg_profit = []

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
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        chg_profit.append(profit[i+1]-profit[i])
                      
#evaluate the max and min from the list made
amtinc = max(chg_profit)
amtdec = min(chg_profit)

#using the index, 
great_inc = chg_profit.index(max(chg_profit))+1
great_dec = chg_profit.index(min(chg_profit))+1

      
result = (
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {row_count}\n"
    f"Total: ${sum(profit)}\n"
    f"Average Change: ${round(sum(chg_profit)/len(chg_profit),2)}\n"
    f"Greatest Increase in Profits: {month_count[great_inc]} (${(str(amtinc))})\n"
    f"Greatest Decrease in Profits: {month_count[great_dec]} (${(str(amtdec))})\n"
)
print(result)

#Open Outputfile and add budge analysis results
with open(OutputFileName, "w+") as txt_file:
   txt_file.write(result)
   txt_file.close()