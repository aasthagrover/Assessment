# Question 2-Extra Credit Question

#Read data from the csv File
import os
x = input()
file=os.path.normpath(os.path.join(x, 'data.csv'))
import pandas as pd
read_data = pd.read_csv(file)

# Group the data by Claim utilization Day count &
#Count the number of claims for each category where  categories are made when Claim utilization days are same.

total_claims_for_eachnumberof_utilization_day = pd.DataFrame(read_data.groupby('Claim Utilization Day Count')['Claim number'].count())
total_claims_for_eachnumberof_utilization_day['Utilization Range'] = total_claims_for_eachnumberof_utilization_day.index
total_claims_for_eachnumberof_utilization_day.columns = ['Counts','Utilization Range']

# Make a list of all the Claim Utilization days.
all_utilization_day_ranges = []

for r in range(1,max(total_claims_for_eachnumberof_utilization_day['Utilization Range'])+1):
    all_utilization_day_ranges.append(r)
    
# Calculate the sum of all the claims for any number of the Claim Utilization days  
total_sum_of_all_claims = total_claims_for_eachnumberof_utilization_day.loc[total_claims_for_eachnumberof_utilization_day['Utilization Range'].isin(all_utilization_day_ranges),'Counts'].sum()


# Make a list 'sum_of_claims_over_each_utilization_range' which contains the sum of the number of claims for each Claim Utilization day range.
sum_of_claims_over_each_utilization_range = []

# The categories for Claim Utilization day range are as follows: 0,1,2,3,4,5,6-10,11,30, greater than equal to 30 days
#all_ranges=[[0],[1],[2],[3],[4],[5],list(range(6,11)),list(range(11,31)),list(range(30,max(total_claims_for_eachnumberof_utilization_day['Utilization Range'])+1))]

range6_10=[]
range11_30=[]
range30_plus=[]

for value in range(0,6):
    sum_of_claims_over_each_utilization_range.append(total_claims_for_eachnumberof_utilization_day.loc[total_claims_for_eachnumberof_utilization_day['Utilization Range']==value,'Counts'].sum())

for i in range(6,11):
    range6_10.append(i)
    
for j in range(11,31):
    range11_30.append(j)
    
for k in range(30,max(total_claims_for_eachnumberof_utilization_day['Utilization Range'])+1):
    range30_plus.append(k)
    
all_ranges=[range6_10,range11_30,range30_plus]

for item in all_ranges:
    sum_of_claims_over_each_utilization_range.append(total_claims_for_eachnumberof_utilization_day.loc[total_claims_for_eachnumberof_utilization_day['Utilization Range'].isin(item),'Counts'].sum())
    
    
# Make a list 'count_list' which contains the percentages of claims in each category range of Claim Utilization Day.
percentage_list=[]

for i,count in enumerate(sum_of_claims_over_each_utilization_range):
    percentage_list.append((count*100)/total_sum_of_all_claims)
    

# Make a dataframe which contains teh Claim Utilization Day Range, Count of claims for each Utilization Day Range, 
# Percentage of Claims for each range
final_frame=pd.DataFrame({'Utilization Range':["0","1","2","3","4","5","'6-10'","'11-30'","30 Plus"],'Counts':sum_of_claims_over_each_utilization_range,'Percentages':percentage_list})
col=final_frame.columns.tolist()
final_columns=[col[2],col[0],col[1]]

try:
    final_frame[final_columns].to_csv('output2.csv',index = False)   
except OSError:
    pass
    os.remove(filename)
    final_frame[final_columns].to_csv('output2.csv',index = False)