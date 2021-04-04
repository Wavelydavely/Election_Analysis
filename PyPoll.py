print("HELLO WHIRLED")

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
# Winner/Stats
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
# Iterate through candidate list
for candidate_name in candidate_votes:
    # Retreive vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, set candidate, votes, & percentage to winning...
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    # Print the candidate name & percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)


# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percdentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
