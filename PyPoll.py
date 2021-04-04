print("HELLO WHIRLED")

# Add our dependencies
import csv
import os

# Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Counter/Tally
total_votes = 0
candidate_options = []
candidate_votes = {}
# Winner/Stats
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file with reader function
with open(file_to_load) as election_data:  
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

# Save results to text file.
with open(file_to_save, "w") as txt_file:

    # Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save final vote count to text file
    txt_file.write(election_results)


    # Determine vote count & percentage of votes for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        # Save & print candidate names, percentages, & totals
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning candidate, percentage, & total
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true, set candidate, votes, & percentage to winning...
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        # Assign winning results to variable
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
            
    print(winning_candidate_summary)

    # Save winning results to text file
    txt_file.write(winning_candidate_summary)