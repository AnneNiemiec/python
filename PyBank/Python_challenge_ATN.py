f = open("PyBank/Resources/budget_data.csv","r")
print (f.readline())
print (f.readline())
print (f.readline())
print (f.readline())

    #set variables 
x,y,z= "Date", "Profit", "Losses"
months=0
total_amounts=0

#The net total amounts of "Profit/Losses" over the entire period
for i in f:
    months=months+1
    Anne=i.split(",")
    total_amounts=total_amounts + int(Anne[1])
print ("Profit/Losses")
print(total_amounts)

#how many months are in the dataset
print("Months")
print(months)

#split out profit/losses
z="Jan-2010,867884"
print(Anne)

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes; by month (i.e. Februrary-January)
# Look for largest and smallest value within
print(df)
column_name="Profit"
print(column_sum)

print(df)
column_name="Losses"
print(column_sum)

Date= str(budget_data[0])
Profit=int(budget_data[1])
Losses=int(budget_data[2])

monthly_total_profit=(profit sum
monthly_total_losses=(losses sum
monthly_change= (profit-losses) 
profit_percent_change=(profits/ monthly_total_profit)*100
losses_percent-change=(losses/monthly_total_losses) *100

def subtract(1-2):
    return 1-2
answer=subtract(x,x)
    print(answer)


# The greatest increase in profits (date and amount) over the entire period
print(f"x for [Date]")
print (f"x for [Amount]")

# The greatest decrease in losses (date and amount) over the entire period
print(f"x for [Date]")
print (f"x for [Amount]")
