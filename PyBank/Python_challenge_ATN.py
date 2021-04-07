# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
import os
import csv

filepath=r'C:\Users\Brad\Desktop\03-Python\PyBank\Resources\budget_data.csv'

#set variables 
months=0
total_amounts=0
avg_value=0
biggest_profit_increase=0
biggest_profit_decrease=0
biggest_profit_increase_month=""
biggest_profit_decrease_month=""

#The net total amounts of "Profit/Losses" over the entire period
month_list = []
profit_losses = []

#search through csv file
with open(filepath)as csvfile:
    csvreader=csv.reader(csvfile)
    #read header
    header=next(csvreader)
    first_month=next(csvreader)
    months=months+1
    total_amounts=total_amounts+float(first_month[1])
    prior_month_totals=float(first_month[1])

#confirm file object
    print(csvreader)

#loop through rows
    for row in csvreader:
        months=months+1
        total_amounts=total_amounts + int(row[1])
        month_list.append(row[0])
        profit_losses.append(int(row[1])-prior_month_totals)

        #Track the net change
        current_difference=int(row[1]) - prior_month_totals
        prior_month_totals=int(row[1])

        #find the biggest profit change
        if (current_difference > biggest_profit_increase):
            biggest_profit_increase = current_difference #if index = 2, then current_difference =66264
            biggest_profit_increase_month= row[0]

        if (current_difference < biggest_profit_decrease):
            biggest_profit_decrease = current_difference 
            biggest_profit_decrease_month=row[0]
#Change value
    avg_value=sum(profit_losses)/len(profit_losses)

f"Financial Analysis\n ==============="

f"Total Months: ${months}"

f"Total: ${total_amounts:.2f}"

f"Average Change: ${avg_value:.2f}"

f"Greatest increase in profit: {biggest_profit_increase_month} ${biggest_profit_increase}"

f"Greatest decrease in profit: {biggest_profit_decrease_month} ${biggest_profit_decrease}"

text_file=(
f"Financial Analysis\n ===============\n"

f"Total Months: ${months}\n"

f"Total: ${total_amounts:.2f}\n"

f"Average Change: ${avg_value:.2f}\n"

f"Greatest increase in profit: {biggest_profit_increase_month} ${biggest_profit_increase}\n"
f"Greatest decrease in profit: {biggest_profit_decrease_month} ${biggest_profit_decrease}\n")

print (text_file)

with open("PyBank\Resources\Pybank_ATN.txt","w") as csvfile:
    csvfile.write(text_file)