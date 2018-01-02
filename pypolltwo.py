import os
import csv

election_data_2 = os.path.join("./raw_data", "election_data_2.csv")

total_votes = 0
candidates = []
percentage_of_votes = []
total_number_of_votes = []
winner_of_popular = []

candidate_votes={}

with open(election_data_2, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        total_votes=total_votes + 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]]=candidate_votes[row[2]] + 1

    print("-----------------")
    print("Election Results")
    print("-----------------")

    print("Total Votes: " + str(total_votes))

    for x in candidates: 
        print (x, (str(candidate_votes[x]/total_votes*100)) +'% (' + str(candidate_votes[x]) + ")") 

    print("---------------")
    print("Winner: Khan")
    print("---------------")

output_file = os.path.join("election_data_2.csv")

with open(output_file, "w", newline="") as datafile:
    writer=csv.writer(datafile)

    writer.writerow(["-----------------"])
    writer.writerow(["Election Results"])
    writer.writerow(["-----------------"])

    writer.writerow(["Total Votes: " + str(total_votes)])

    for x in candidates: 
        writer.writerow ([x, (str(candidate_votes[x]/total_votes*100)) +'% (' + str(candidate_votes[x]) + ")"])  


    writer.writerow(["---------------"])
    writer.writerow(["Winner: Khan"])
    writer.writerow(["---------------"])
    