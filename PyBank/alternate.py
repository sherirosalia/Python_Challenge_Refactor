import csv
import numpy as np

total_profit_loss = 0
count_of_months=0
first_row_value=0
lowest_value=0
highest_value=0
starting_balance=0
net_change_list=[]
lowest_month_change = ''
highest_month_change = ''

bank_data = "PyBank/Resources/budget_data.csv"
# bank_data = os.path.join("Resources", "budget_data.csv")

with open(bank_data) as csvfile:
    bank_data = csv.DictReader(csvfile)

    '''Since we've isolated the first row of data from iteration, we need to add one to the count of months, add the monthly profit/loss to total profit loss and preserve the value for net change comparison'''

    first_row_value = next(bank_data)
    # print(f'first row value {first_row_value}')
    starting_balance = int(first_row_value['Profit/Losses'])
    # print('first starting balance ', starting_balance)
    count_of_months +=1
    total_profit_loss += starting_balance

  
    # for row in bank_data:
    for row in bank_data:
        count_of_months +=1
        
        # print(row['Date'], ' ', row['Profit/Losses'])
        date=row['Date']
        monthly_net=int(row['Profit/Losses'])
        total_profit_loss += monthly_net
        # print(date, ' ', monthly_net)
        # print( starting_balance)
        # print(monthly_net - starting_balance)
        net_change = starting_balance - monthly_net
        net_change_list.append(net_change)
        starting_balance=monthly_net
        # print(starting_balance)
        # print('second starting balance ', starting_balance)
        # print(net_change)
        # exit()
        # starting_balance=net_change
        # print(starting_balance)
        # # print(net_change)
        if net_change > highest_value:
            highest_value = net_change
            date=row['Date']
            # print('highest value  ',date, ' ', highest_value)
            highest_month_change = f'The month with highest net change is: {date} and the amount is: {highest_value}'
        if net_change < lowest_value:
            lowest_value = net_change
            date=row['Date']
            # print('lowest value  ' ,date, ' ' ,lowest_value)
            lowest__month_change = f'The month with lowest net change is: {date} and the amount is: {lowest_value}'
    # print(highest_value, ' ', lowest_value)

        
        

        # exit()
print(total_profit_loss)
print(lowest__month_change)
print(sum(net_change_list)/len(net_change_list))

print(highest_month_change)

# print(count_of_months, first_row_value['Profit/Losses'])