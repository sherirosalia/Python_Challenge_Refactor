import os
import csv
''' requirements for the latest iteration of python challenge does not require inclusion of county data, only the winning votes (2023)'''
'''
PROMPT ASKS FOR:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote
'''

# poll_data = 'Starter_Code/PyPoll/Resources/election_data.csv'
# poll_data = os.path.join("PyPoll","Resources", "election_data.csv")
poll_data = "PyPoll/Resources/election_results.csv"
analysis_file = 'PyPoll/analysis/analysis.txt'

total_number_of_votes_cast = 0
candidate_list = []
candidate_dict = {}
# candidate_list_of_dictionaries = []

with open(poll_data, 'r') as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
    
    for row in reader:
        # print(row)
        total_number_of_votes_cast+=1
        candidate = row[2]
        # county = row[1]
        
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_vote = 1
            candidate_dict[candidate] = candidate_vote
        
        else:
            
            candidate_dict[candidate] +=1 

print("first candidate dictionary not sorted: --- ", candidate_dict)
candidate_dict = sorted(candidate_dict.items(), key=lambda x:x[1])
print("second candidate dictionary sorted: ---" ,candidate_dict)
winning_candidate=candidate_dict[-1][0]
print("winning candidate:  --", winning_candidate)
winning_candidate_votes =candidate_dict[-1][1]

with open(analysis_file, "w") as analysis_txt:

    analysis_data = (
        f'ELECTION RESULTS:\n'
        f'*******************************************\n'
        f'total votes for all candidates: {total_number_of_votes_cast}\n'
        f'*******************************************\n'
        f'The winner of the election based on popular vote is:{winning_candidate} with {winning_candidate_votes} in vote count \n'
        f'*******************************************\n'
        f'The breakdown of votes for all candidates: \n'
    )

    analysis_txt.write(analysis_data)

    for candidate_votes in candidate_dict:
        # print("value: " , candidate_votes[1])
        candidate_name = candidate_votes[0]
        candidate_total_votes = candidate_votes[1]
        candidate_percentage = float(candidate_votes[1])/float(total_number_of_votes_cast) *100
        # print("percentage of votes: ", candidate_percentage)

        candidate_voting_totals = f"{candidate_name}: {candidate_percentage:.3f}% ({candidate_total_votes})\n"
        print(candidate_voting_totals, end="")
        analysis_txt.write(candidate_voting_totals)







    print(analysis_data)

  
# print(candidate_dict) 
# print(total_number_of_votes_cast)
# print(candidate_list)