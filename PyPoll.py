# The data we need to retrieve.
# Add our dependencies
import csv
import os
# Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:  
    #headers = (next(csvreader))

    # To do: read and analyze the data here)
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    # Print header row
    headers = next(file_reader)
    print(headers)
    
    

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percdentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
