import os
import csv
# file path
election_path = os.path.join("Resources", "election_data.csv")
# file output
file_output = "analysis/election_analysis.txt"

totalnum_votes = 0
candidate = []
candidate_list = []
candidate_votes = {}
winner = ""
winning_count = 0


with open(election_path, "r") as f:
    reader = csv.reader(f, delimiter = ',')
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
print("Election Results")
print("-----------------------------------")
print("Total Votes: " + str(totalnum_votes))
print("-----------------------------------")
# print the results
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

          voter_results = (f'{candidate}: {vote_percentage:.3f}% ({votes})') 
          print(voter_results)
        # save results into file_output
          text.write(voter_results + "\n")


      # Output the results to election_analysis.txt
      text.write("\n---------------------------------------\n")
      text.write("Winner: " + winning_candidate + "\n")
      text.write("---------------------------------------\n")

print("----------------------------")
print("Winner: " + winning_candidate)
print("----------------------------")



   


  
   
    




       
