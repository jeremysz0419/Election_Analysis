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

#Open election results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read and pring the header row.
    headers = next(file_reader)
    print(headers)