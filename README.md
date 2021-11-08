# Election_Analysis
## Overview
The purpose of this analysis was to visualize the results of an election for auditing purposes. Based on the data we received, we needed to determine and display the following results: 
1. The Winner of the Election 
2. The County with the Most Votes
3. Percentage and Amount of Votes Each Candidate Received
4. Percentage and Amount of Votes were Cast fom Each County

## Election Audit Results 
Please see below for the results of our analysis. 
## Candidacy Results 
* Charles Capser Stockam received **23.0%** of the votes (**85,213** Votes)
* Diana DeGette received **73.8%** of the votes (**272,892** Votes)
  * Diana DeGette is the overwhelming **Winner** of this election 
* Raymon Anthony Doane received **3.1%** of the votes (**11,606** Votes)
## County Results
* Jefferson county represented **10.5%** of all votes (**38,855** Votes)
* Denver county represented **82.8%** of all votes (**306,055** Votes)
  *   Most of the votes came from **Denver** county with **82.8%** of all votes coming from Denver
* Arapahoe county represented **6.7%** of all votes (**24,801** Votes)

## Election Audit Summary
The turnout of this election is overwhelming towards one candidate and one county. Diana DeGette swept the election by a large margin. Most of the votes came from the county of Denver, which should hold true in most cases as Denver is the most densely populated county out of the three. However, for future cases, it may be nice to provide the population of each county to determine the voter turnout from each county. 
Our script follows a logic in which the variables can be changed, added, and formatted in a way in which it could be used for other elections. For example, all of our "elements" are tracked and kept within a list and dictionary (see below):
```
  entity_options = []
  entity_votes = {}
  
  
   for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the entity name from each row.
        entity_name = row[x]
        if entity_name not in entity_options:
            entity_options.append(entity_name)
            entity_votes[entity_name] = 0

        entity_votes[entity_name] += 1
```
As long as the data of the election is formatted in rows by individual votes, the code logic above can be used to extract election results and any sub-categories of that election. For example, if our data included a new row of data by "age group" or "job status", we would simply change the variable "x" within ```entity_name = row[x]``` to extract the information from that row. The rest of the script would extract a list of all the different options within the row and aggregate the amount of rows (or votes) within that option to the ```entity_votes``` dictionary. Say we enter a row containing the job status of each voter ("unemployed", "student", "part-time", "full-time"), the script will automatically show the different job statuses and a dictionary showing the amount of votes each job status had. 
