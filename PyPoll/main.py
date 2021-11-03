import os
import csv

# -- define function to fix percentage format to 3 decimal points ---
def fPercent(num):
    num = "{:.3%}".format(num)
    return num

# dictionary for greatest increase and decrease and other variables
candidate_vote = []
candidate_votecnt = []
candidate_votepct = []
Total_Votes = 0
WinnerCount = 0

# specify input file name and path

currt_dir = os.getcwd()
read_path = './Resources'
election_csv = os.path.join(currt_dir,read_path,'election_data.csv')

# specify output file name and path
#save_path = '/Users/Pulast/data boot camp/projects/python-challenge/pyPoll/Analysis'
save_path = './Analysis'
file_name = "election_analysis.txt"
OutputFileName = os.path.join(currt_dir,save_path,file_name)
print(OutputFileName)

# Read the input file
with open(election_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    data = list(csvreader)
    
    # Total Months in the file
    row_count = len(data)

# Read each row of data after the header
    for row in data:

        #total months
        Total_Votes = Total_Votes + 1

        #Find greatest increase and decrease
        if row[2] not in candidate_vote:

            # this is the first candidate and add to the list
            candidate_vote.append(row[2])
            candidate_votecnt.append(1)

        # candidate name is in the list and repeating
        else:
            candidateindex = candidate_vote.index(row[2])
            candidate_votecnt[candidateindex]= candidate_votecnt[candidateindex] +1

   # calculate the percentage of votes for each candidate
for i in range(len(candidate_votecnt)):
       candidate_votepct.append(candidate_votecnt[i]/Total_Votes)            

 # write total votes in a variable              
       total_votes_result = (
                  f"\nElection Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {Total_Votes}\n"
                   f"----------------------------\n"
                   )

print(total_votes_result)


   # write each candidate's info

#Open Outputfile and add budge analysis results
with open(OutputFileName, "w+") as csvfile:

    # write in total votes in file and print on terminal
    
    csvfile.write(total_votes_result)

    for i in range(len(candidate_vote)):
   # print(f"{candidate_vote[i]}: {fPercent(candidate_votepct[i])} : ({candidate_votecnt[i]})")
        candidate_info = (
         f"{candidate_vote[i]}: {fPercent(candidate_votepct[i])} : ({candidate_votecnt[i]})\n"
           )
       #print candidate info in file and terminal
        print(candidate_info)
        csvfile.write(candidate_info)
    
    # calculate winner who got most number of votes
    for i in range(len(candidate_votecnt)):
        if candidate_votecnt[i] > WinnerCount:
            WinnerCount = candidate_votecnt[i]
            winner = candidate_vote[i]
#print winner result
        winner_result =(
                   f"----------------------------\n"
                   f"Winner : {winner}\n"
                   f"----------------------------\n"
                   )

    print(winner_result)
    csvfile.write(winner_result)
    csvfile.close()