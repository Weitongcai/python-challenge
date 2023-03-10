import os
import csv
# Input file path
election_path = os.path.join("Resources", "election_data.csv")
# Output file path
file_output = "analysis/election_analysis.txt"

totalnum_votes = 0
candidate = []
candidate_list = []
candidate_votes = {}
winner = ""
winning_count = 0

# Read input file path
with open(election_path, "r") as f:
    reader = csv.reader(f, delimiter = ',')
    # Stores the header row
    header_row = next(reader)

    for row in reader :
        # Total number of votes cast
        totalnum_votes += 1
        # A complete list of candidates who received votes
        candidate = row[2]
        if candidate not in candidate_list :
           candidate_list.append(candidate)
           candidate_votes[candidate] = 0

        candidate_votes[candidate] = candidate_votes[candidate] + 1

# Print the election results        
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: " + str(totalnum_votes))
print("-----------------------------------")

# Output the results to election_analysis.txt
with open(file_output, "w",newline = '' ) as text:    
      text.write("Election Results\n")
      text.write("-----------------------------------\n")
      text.write("Total Votes: " + str(totalnum_votes)+ "\n")
      text.write("------------------------------------\n")


#The percentage and total number of votes each candidate won
      for candidate in candidate_votes :
          votes = candidate_votes.get(candidate)
          vote_percentage = float(votes) / float(totalnum_votes) * 100

          if (votes > winning_count) :
              winning_count = votes
              winning_candidate = candidate
        #Print the voter and his/her results as required
          voter_results = (f'{candidate}: {vote_percentage:.3f}% ({votes})')  
          print(voter_results)
        # Output the voter and his/her results to election_analysis.txt
          text.write(voter_results + "\n")


      # Output the results to election_analysis.txt
      text.write("\n---------------------------------------\n")
      text.write("Winner: " + winning_candidate + "\n")
      text.write("---------------------------------------\n")
# Print the winner results as required
print("----------------------------")
print(f"Winner: " + winning_candidate)
print("----------------------------")



   


  
   
    




       
