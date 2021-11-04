#Data to be retrieved
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. The winner of election based on popular vote
import csv
import os 
#Assign variable to election results data
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign variable to analysis txt
file_to_save = os.path.join("analysis","election_analysis.txt")
#Initialize vote counter
total_votes = 0 
#Create empty list for all candidates
candidate_options = []
#Create candidate vote dictionary
candidate_votes = {}
#Winning Candidate & Winner Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open election results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read and pring the header row.
    headers = next(file_reader)
    #print each row in CSV
    for row in file_reader:
        #For each row, tally one vote
        total_votes += 1
        #candidate name extracted
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #add to candidate_options
            candidate_options.append(candidate_name)
            #track vote count
            candidate_votes[candidate_name] = 0
        #tally votes outside of if 
        candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes: 
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        print(f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n") 
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n"     
        )
        print(winning_candidate_summary)
 
    print(f"{winning_candidate} received {winning_percentage}% of the votes with a total of {winning_count} votes")

print(candidate_votes)