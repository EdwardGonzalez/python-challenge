import csv
import os
import pandas as pd

Link = "C:/Programas/Homework3/Instructions/PyBank/Resources/budget_data.csv"

# Import the books.csv file as a DataFrame
BData = pd.read_csv(Link, encoding="utf-8")

#The total number of months included in the dataset
TotalMonth = len(BData["Date"].unique())

#The net total amount of "Profit/Losses" over the entire period
Sum = BData["Profit/Losses"].sum()

#The average of the changes in "Profit/Losses" over the entire period
Avg = BData["Profit/Losses"].mean()

#The greatest increase in profits (date and amount) over the entire period
indexMax=BData["Profit/Losses"].idxmax()
mMax = BData.at[indexMax,'Date']
Max = BData["Profit/Losses"].max()

#The greatest decrease in losses (date and amount) over the entire period
indexMin=BData["Profit/Losses"].idxmin()
mMin = BData.at[indexMin,'Date']
Min = BData["Profit/Losses"].min()

#Report Printing

print ("Financial Analysis")
print("-----------------------------")
print (f'Total Months: {TotalMonth}')
print (f'Total: ${Sum}')
print (f'Average Change: ${Avg}')
print (f'Greatest Increase in Profits: {mMax} (${Max})')
print (f'Greatest Decrease in Profits: {mMin} (${Min})')