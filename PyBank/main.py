import os
import csv

 #declared variable

total_months=0
month_list=[]
net_total=0
total_list=[]
average_change=0
budget=[]
pnl=[]
pnl_change =[]
pro_loss=0
greatest_increase_month = ""
greatest_decrease_month = ""


#path to source file
csvpath = os.path.join('Resources','budget_data.csv')

#open file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        #print(row)
        month_list.append(row[0])
        net_total += int(row[1])
        pnl.append(int(row[1]))


total_months=len(month_list)

#average
i = 0
n=0

for i in range(total_months -1):
    n = i + 1
    pro_loss += int(pnl[n]) - int(pnl[i])
    pnl_change.append(int(pnl[n]) - int(pnl[i]))


#Calculations

average_change = ( int(pro_loss)  / (int(total_months - 1)))
Greatest_Increase_Profits = max(pnl_change)
Greatest_Decrease_Profits = min(pnl_change)


def findChange(pnl_value):

    for i in range(len(pnl_change)):
        if pnl_change[i] == int(pnl_value):
            return month_list[i + 1]
            break



greatest_increase_month = findChange(int(Greatest_Increase_Profits))
greatest_decrease_month = findChange(int(Greatest_Decrease_Profits))



# print summary with the results
print("Financial Analysis")
print("-" * 25)
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${Greatest_Increase_Profits})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${Greatest_Decrease_Profits})")

# open a new text file with "write" mode.
file = open("financial_report.txt", "w")

# write the results to the text file
file.write("Financial Analysis\n")
file.write("-" * 25)
file.write(f"\nTotal Months: {total_months}\n")
file.write(f"Total: ${net_total}\n")
file.write(f"Average Change: ${average_change}\n")
file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${Greatest_Increase_Profits})\n")
file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${Greatest_Decrease_Profits})\n")
# make sure the file is closed
file.close()