# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# 2: Track the largest county and county voter turnout.
largest_County_Turnover = ""
largest_count = 0
largest_percentage = 0
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # 3: Extract the county name from each row.
        county_name = row[2]

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

           # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
    county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"county Votes: {county_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")

    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        county_votes = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(county_votes) / float(total_votes) * 100
        
        # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({county_votes:,})\n")
        print(county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_votes > largest_count) and (vote_percentage > largest_percentage):
            largest_count = county_votes
            largest_county = county_name
            largest_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_summary = (
        f"-------------------------\n"
        f"largest: {largest_county}\n"
        f"largest Vote Count: {largest_count:,}\n"
        f"largest Percentage: {largest_percentage:.1f}%\n"
        f"-------------------------\n")
    print(largest_county_summary, end="")
 # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_summary)
 