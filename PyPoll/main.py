import csv
import os
import pandas as pd

Link = "C:/Programas/Homework3/Instructions/PyPoll/Resources/election_data.csv"

# Import the books.csv file as a DataFrame
BDPoll = pd.read_csv(Link, encoding="utf-8")

#The total number of votes cast
TotalVote = len(BDPoll["Voter ID"].unique())
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
Nombre = BDPoll["Candidate"].unique()
SumVotos = BDPoll["Candidate"].value_counts()
SumPor = BDPoll["Candidate"].value_counts()/len(BDPoll["Voter ID"].unique())*100

#Report Printing

print ("Election Results")
print("-----------------------------")
print (f'Total Votes: {TotalVote}')
print("-----------------------------")
i=0
for i in range(len(Nombre)):
    print (f' {Nombre[i]}: {SumPor[i]}% ({SumVotos[i]})')
print("-----------------------------")
print ("Winner: "+ Nombre[0])
print("-----------------------------")