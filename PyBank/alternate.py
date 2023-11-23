import csv
#import os

## declarations explained in comments after csv is opened
total_profit_loss = 0
count_of_months=0
first_row_value=0
lowest_value=0
highest_value=0
starting_balance=0
net_change_list=[]
lowest_month_change = ''
highest_month_change = ''

## relative path of csv file assigned to bank data variable
bank_data = "PyBank/Resources/budget_data.csv"

##  alternate way to open file. uncomment import os statement above and configure for local file configuration 
# bank_data = os.path.join("Resources", "budget_data.csv")
''' Link to csv reader module documentation: https://docs.python.org/3/library/csv.html'''
with open(bank_data) as csvfile:
    # using DictReader does not generate a header row like reader does
    bank_data = csv.DictReader(csvfile)

    '''Code below isolates the first row of data from iteration. So that we can preserve the first month profit and loss for net change comparison to the first row of monthly data in the for loop below'''

    first_row_value = next(bank_data)
    
    # print(f'first row value {first_row_value}')

    '''Since the first row is isolated from iteration (ie for loop below), we need to preserve values for calculations. Code below adds one to the count of months, add the first month profit loss to to total profit loss and preserve the first month net/loss or profit value for net change comparison'''
    starting_balance = int(first_row_value['Profit/Losses'])
    # print('first starting balance ', starting_balance)
    count_of_months +=1
    '''total_profit loss adds the profit loss value for month being evaluated to the variable of the same name listed above to preserve the value because if we don't, after the with open statement and loop ends, it will not be retrievable... we will also need to do this in the for loop code below to preserve values from future month data'''
    total_profit_loss += starting_balance

    ''' Looping through rows which actually starts with the second month  instead of the first as explained above '''
    # for row in bank_data:
    for row in bank_data:
        count_of_months +=1
        ## debugging print statement
        # print(row['Date'], ' ', row['Profit/Losses'])
        date=row['Date']
        ## monthly net is the profit loss value for row that is being evaluated
        monthly_net=int(row['Profit/Losses'])

        ''' total_profit loss adds the profit loss value for month being evaluated to the variable of the same name listed above to preserve the value because if we don't, after the for loop ends, it will not be retrievable'''
        total_profit_loss += monthly_net
        ## debugging print statements
        # print(date, ' ', monthly_net)
        # print( starting_balance)
        # print(monthly_net - starting_balance)

        '''net_change variable deducts the starting balance which in this case is zero, from the first month's profit loss value'''
        net_change = starting_balance - monthly_net

        ''' now that we have the net change for the first month of data, we add it to the net change list which was initialized above and outside of the with open statement so that it can be retrievable after the with open closes '''
        net_change_list.append(net_change)

        '''preserve the monthly net value from the first row for comparison purposes as we loop through the rest of the monthly data in the for loop below (see variable declarations above)'''
        starting_balance=monthly_net

        ## debugging print statements
        # print(starting_balance)
        # print('second starting balance ', starting_balance)
        # print(net_change)

        '''exit function will stop script so that we can isolate the first two rows and see if our calculations above are working when utilizing debugging print statements'''

        # exit()
        ## debugging print statements which will check for starting balance calculation and net change for each month in all rows when exit statement is disabled
        # starting_balance=net_change
        # print(starting_balance)
        # # print(net_change)

        '''conditional statements below obtain lowest and highest net change and preserve in variable, we are now looping through every row after the first one, so the values will be compared each month and replace what is in the variable declared as higest or lowest value depending on the results found in each month of data'''


        if net_change > highest_value: # if the net change from previous row is greater than the highest value stored in variable declarations above. on the first loop (2nd month) this will be compared to the first month profit and loss. As we continue to iterate through monthly data this will change. If the net change is not greater than the highest value, this will be bypassed and the program will move on to our next conditional statement
            highest_value = net_change #if the conditional statement is activated, (meaning that we have a new highest value) because the net change for given month is greater than what was previously the highest value, we need to update the highest_value variable to reflect the latest net change. We can do this by simply re-assigning the new amount to the highest_value variable
            date=row['Date'] #the prompt wants the month, so we need to make sure we have that.

            ## debuging print statement to be sure we are retrieving expected values
            # print('highest value  ',date, ' ', highest_value)

            '''as the conditional statement is evaluated row by row, the highest net/profit is preserved along with the date'''

            '''print statement assigned to variable highest_month_change - above the with open statement to preserve for sending to text file later '''
            highest_month_change = f'The month with highest net change is: {date} and the amount is: {highest_value}'

        '''all the same principles described for the highest value are applied in the next conditional statement which is looking for the lowest net change'''
        if net_change < lowest_value:
            lowest_value = net_change
            date=row['Date']
            # print('lowest value  ' ,date, ' ' ,lowest_value)
            lowest__month_change = f'The month with lowest net change is: {date} and the amount is: {lowest_value}'

    '''debugging print statement placed as such that the for loop is closed by lack of indentation and therefore access the results of our logic. Note it is still within the with open function meaning that the csv file is still available for evaluation - it doesn't necessarily need to be placed there. It can be un-indented as seen in debugging statements below'''
    # print(highest_value, ' ', lowest_value)    
        
## debugging print statements
# print(total_profit_loss)
# print(lowest__month_change)

''' the average net change calculation needs to be based on 85 months even though we have 86 months of data, because the first month in our csv did not have net change data available for us to use. By using the len() function, we access the count of the net change list which is 85 months of data '''
average_net_change =sum(net_change_list)/len(net_change_list)
# print(average_net_change)

# print(highest_month_change)

# print(count_of_months, first_row_value['Profit/Losses'])
'''f strings are available in python to make formatting and printing data more user friendly. Link to documentation: https://docs.python.org/3/tutorial/inputoutput.html'''
analysis_metrics = (f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total number of months: {count_of_months} \n"
    f"Total profit/loss: {total_profit_loss} \n"
    f" {highest_month_change} \n"
    f" {lowest__month_change}\n"
    f" The average net change is: {average_net_change:.2f} \n")
'''prompt requires print to terminal and text file'''
print(analysis_metrics)
output_file = "analysis_metrics.txt"
with open(output_file, "w") as analysis_to_write:
    analysis_to_write.write(analysis_metrics)