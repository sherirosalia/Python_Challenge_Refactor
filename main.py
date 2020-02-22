#refactored script

# #dependencies

import os
import csv
#import operator for running code on line 63
import operator


#csv file with election data
election_data=os.path.join("election_results.csv")

#variables
total_votes = 0
county_votes = {}
candidates = {}

#open csv
with open(election_data) as election_data:
    readCSV = csv.reader(election_data, delimiter=',')
    # Read the header
    header = next(readCSV)
    print('The headers are: {header}')
    
    #loop through data to append dictionaries
    for row in readCSV:
        # Add to the total vote count
        total_votes = total_votes + 1

        county= row[1]
        candidate = row[2]

            
        if county not in county_votes:
            # setting default value 
            county_votes[county] = 0
        #appending regardless of whether county existed before or not
        # because we are outside of the if statment (forcing function).    
        county_votes[county] += 1
        
        #duplicate above comments substituting candidate
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1


    # print(county_votes)   
    # print(f'Total Votes are: {total_votes}') 
    # print(county_votes.items())


    #county winner
    County_Most_Votes = (max(county_votes, key=county_votes.get))
    
    #candidate winner
    candidate_top_votes = (max(candidates, key=candidates.get))
    # print(f'Candidate with most votes is: {candidate_top_votes}')

  
    for candidate in sorted(candidates, key=candidates.get):
        # print("%d '%s'" % (candidates[candidate], candidate))
        # print("%s'%d'" % (candidate, candidates[candidate], )) 
        
        candidate_by_name = candidate
        votes_per_candidate = candidates[candidate]
        candidate_vote_percent = votes_per_candidate/total_votes * 100
        print(f'{candidate_by_name} votes: ({votes_per_candidate:,}){candidate_vote_percent:.1f}% ')
        candidate_tally = ("%s'%d'" % (candidate, candidates[candidate], ))
        print(candidate_tally)

    #function below allows us to call the percentage and tallies for counties and candidates
    #avoids having to break up our write to file statement so that we can access loop data


    def access_dictionary(dictionary, total):
        layout = ''
        #we don't need to define the dictionary in function
        for item in dictionary:
            tally = dictionary[item]
            percentage=tally/total *100
            tallies = ("%s'%d'" % (item, dictionary[item], ))
            layout = layout + f'{item} votes: ({tally:,}) percentage: {percentage:.1f}% \n'
            #print(tallies)
            # print(f'{item} votes: ({tally:,}) percentage: {percentage:.1f}% ')
        return layout
        #common pattern to establish empty string, add to and return in function

   
    access_dictionary(candidates, total_votes)
    print(f'-----------------')
    access_dictionary(county_votes, total_votes)

            
    candidate_data = access_dictionary(candidates, total_votes)
    county_data = access_dictionary(county_votes, total_votes)

    #print to terminal
    print(candidate_data)

    #create text file to save analysis
    results=os.path.join("analysis", "election_analysis.txt")

    with open (results, "w") as txt_file:
        election_talies = (
            f'---Election Tallies ----\n'
            f'------------------------\n'
            f'Total Votes: {total_votes}\n'
            f'------------------------\n'
            f'------------------------\n'
            f'County Votes: \n'
            f'------------------------\n'
            f'{county_data}'
            f'------------------------\n'
            f'------------------------\n'
            f'Largest County Turnout: {County_Most_Votes}\n'
            f'------------------------\n'
            f'------------------------\n'
            f'Candidates: \n'
            f'------------------------\n'
            f'{candidate_data}'
            f'------------------------\n'
            f'------------------------\n'
            f'Winner: {candidate_top_votes} \n'
            f'------------------------\n\n'
            
        )
        print(election_talies, end='')
        txt_file.write(election_talies)

    

    





    

        
        


