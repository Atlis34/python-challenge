# set libraries
import os
import csv

# initialize variables - including dictionary
total_ballots = 0
candidate_votes = {}

# path for csv resource file
election_csv = os.path.join('Resources', 'election_data.csv')

# open file - set delimited
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header and store in variable
    csv_header = next(csvreader)

    # vote counting loop
    for row in csvreader:
        total_ballots += 1
        candidate_name = row[2]
        # add name to dictionary if not present, otherwise increase total votes by 1
        if candidate_name not in candidate_votes:
           candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1
            
# print dictionary to terminal 
print(candidate_votes)

# set election_csv
election_csv = os.path.join('analysis', 'election_analysis.txt')

# initialize winner variables
winner_votes = 0
winner_name = ""

# f-string total number of votes into desired output format
with open(election_csv, "w") as csvfile:
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_ballots}\n"
        f"-------------------------\n")

    # print election results
    print(election_results, end="")

    # write results to csv file
    csvfile.write(election_results)

    # add vote totals and percentages for each candidate
    for candidate_name in candidate_votes: 
        votes = candidate_votes[candidate_name]
        vote_percent = (votes / total_ballots) * 100

        # check each candidate against the highest votes found so far and determine winner
        if votes > winner_votes:
            winner_name = candidate_name
            winner_votes = votes

        # set variable with name, percentage, and total vote count
        voter_output = f"{candidate_name}: {vote_percent:.3f}% ({votes})\n"
        print(voter_output, end="")

        # write to csv file
        csvfile.write(voter_output)

    # create summary variable with winner name formatted properly
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner_name}\n"
        f"-------------------------\n")

    # print winner variable below stats
    print(winning_candidate_summary)

    # write winner to csv file
    csvfile.write(winning_candidate_summary)
