import csv
import os
import numpy as np

new_count = 0
count_of_months = 0
total_profit_loss = 0
monthly_change = 0
month_to_compare = 0
monthly_change_list = []
monthly_change_month_and_amount_dicts = []
# file_to_load =os.path.join("Starter_Code/PyBank/Resources/budget_data.csv")

# with open(file_to_load) as financial_data:
#     reader = csv.reader(financial_data)

#     for row in reader:
#         new_count += 1

# print(new_count)

# exit()

bank_data = "PyBank/Resources/budget_data.csv"
# bank_data = os.path.join("Resources", "budget_data.csv")

with open(bank_data) as csvfile:
    reader = csv.DictReader(csvfile)

    '''Since we've isolated the first row of data from iteration, we need to add one to the count of months, add the monthly profit/loss to total profit loss and preserve the value for net change comparison'''

    first_row_value = next(reader)
    # print(f'first row value {first_row_value}')
    first_month_balance = int(first_row_value['Profit/Losses'])
    count_of_months +=1
    # add first month to track total revenues
    total_profit_loss += first_month_balance
    # establish base value to compare net change for next month
    month_to_compare += first_month_balance
    # print(count_of_months, total_profit_loss)
    monthly_change += first_month_balance
    # print(monthly_change)
    date_amount_dictionary = {
            'date' : first_row_value['Date'],
            'net_change' : int(first_row_value['Profit/Losses'])
        }
    monthly_change_month_and_amount_dicts.append(date_amount_dictionary)
    for row in reader:
        '''debugging print statements'''
        # first_row_value = next(row['Profit/Losses'])
        # print(f'first row value {first_row_value}')
        # print(row['Date'])
        # print(row)
        count_of_months +=1
        current_month = int(row['Profit/Losses'])
        profit = int(row['Profit/Losses'])
        total_profit_loss = total_profit_loss + profit
        pertinant_date = row['Date']

        monthly_net_change = profit - month_to_compare
        # print(f'monthly change: {monthly_net_change}')
        date_amount_dictionary = {
            'date' : pertinant_date,
            'net_change' : monthly_net_change
        }
        monthly_change_list.append(monthly_net_change)
        monthly_change_month_and_amount_dicts.append(date_amount_dictionary)
        month_to_compare = current_month
        # print(monthly_change_month_and_amount)
        


        
        # print(previous_month)

   
    
    ''' set up a function to be passed on to min, max and median so that they can then call it
    '''
    def extract_net_change(net_dict):
        return net_dict['net_change']
    
    '''generic minimum function'''
    def return_minimum(list_of_things, the_extraction_function):
        smallest_x = None
    
        for x in list_of_things:
            # the_value_of_x = the_extraction_function(x)
            # the_value_of_smallest_x = the_extraction_function(smallest_x)
            if smallest_x is None or the_extraction_function(x) < the_extraction_function(smallest_x):
                smallest_x = x

        return smallest_x

        
    average_net_change = sum(monthly_change_list) / len(monthly_change_list)
    greatest_monthly_increase = max(monthly_change_list)
    greatest_monthly_decrease = min(monthly_change_list)

    ''' note: passing function without parens to pass as a parameter to our chosen functions (treating the function extract net change as an object). Another option would be to use a lambda function in it's place (lambda x: x['net_change'])'''
    # for example, uncomment below
    # extract_net_change = lambda x: x['net_change']

    # print(min(monthly_change_month_and_amount_dicts, key = extract_net_change))

    # print(return_minimum(monthly_change_month_and_amount_dicts, extract_net_change ))
    minimum_value = return_minimum(monthly_change_month_and_amount_dicts, extract_net_change )
    print(minimum_value['date'], minimum_value['net_change'])

    maximum_value = (max(monthly_change_month_and_amount_dicts, key = extract_net_change))
    print(maximum_value['date'], maximum_value['net_change'])


    #median
    sorted_values = (sorted(monthly_change_month_and_amount_dicts, key = extract_net_change))
    print(f'number of sorted values {len(sorted_values)}')

    median_index = len(sorted_values)//2
    print('median value: ')
    print(median_index)
    print(sorted_values[median_index])

    #second highest
    second_highest = sorted_values[-1]
    print(f'second highest gain: {second_highest}')

    #second lowest
    second_lowest = sorted_values[1]
    print(f'second lowest gain: {second_lowest}')


    #standard deviation
    standard_deviation =np.std(monthly_change_list)
    print(f'standard deviation is: {standard_deviation}')

    print(total_profit_loss)
    print(f'The number of months: {count_of_months}')
    print((f'greatest monthly increase:{pertinant_date}: {greatest_monthly_increase}'))
    print((f'greatest monthly decrease:{pertinant_date}: {greatest_monthly_decrease}'))
    print((f'average net change: {average_net_change}'))

    # print(monthly_change_month_and_amount_dicts)
 
    # print(f'Total net profit: {total_net_profits}')

    analysis_data = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {count_of_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_net_change:.2f}\n"
    f"Greatest Increase in Profits: {pertinant_date} (${greatest_monthly_increase})\n"
    f"Greatest Decrease in Profits: {pertinant_date} (${greatest_monthly_decrease})\n"
    f"Standard Deviation: {standard_deviation}"
    )
    output_file = "analysis.txt"
    with open(output_file, "w") as analysis_to_write:
        analysis_to_write.write(analysis_data)

 

