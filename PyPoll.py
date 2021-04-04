# Add our dependencies
import csv
import os
# Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Counter
total_votes = 0
candidate_options = []
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:  

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Add to the total vote count and candidate list
    for row in file_reader:       
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
# Determine percentage of votes for each candidate
# 1. Iterate through candidate list
for candidate_name in candidate_votes:
    # 2. Retreive vote count of a candidate
    votes = candidate_votes[candidate_name]
    # 3. Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name & percentage of votes
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percdentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
