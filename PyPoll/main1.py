import os
import csv
from statistics import mean

 #declared variable

total_months=0
month_list=[]
net_total=0
total_list=[]
Average_Change=[]
Greatest_Increase_Profits=[]
Greatest_Decrease_Profits=[]
budget=[]
pnl=[]
pro_loss=0
prev_pnl=0
cur_pnl=0


#path to source file
csvpath=os.path.join('Resources','budget_data.csv')

#open file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        print(row)
        month_list.append(row[0])
        pnl.append(int(row[1]))
        #net_total += int(row[1])
#print(pnl)
        

  


total_months=len(month_list)
#print(total_list)

# print(total_months)
# print(net_total)
# print(pnl)

#average
i = 0
n = 0
pnl_lenght=len(pnl)-1

for i in range(len(pnl_lenght)):
    n=i+1
    prev_pnl=int(pnl[i])
    cur_pnl=int(pnl[n])
    pro_loss += (cur_pnl-prev_pnl)
#print(pro_loss)    
#print(mean(pro_loss))

 

# #greatest increase

    







