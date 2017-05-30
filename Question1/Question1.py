# Question 1

#Read data from the csv File
import os
x = input()
file=os.path.normpath(os.path.join(x, 'data.csv'))
import pandas as pd
read_data = pd.read_csv(file)

#1.Filter Gender code for Males & Females
#2. Group by State codes to count the number of Males & Females in each State.
females=pd.DataFrame(read_data.loc[read_data['Gender Code from Claim'] == 1].groupby('State Code from Claim (SSA)')['Gender Code from Claim'].count())
females['State']=females.index
females.columns=['Females','State']

males=pd.DataFrame(read_data.loc[read_data['Gender Code from Claim'] == 2].groupby('State Code from Claim (SSA)')['Gender Code from Claim'].count())
males['State']=males.index
males.columns=['Males','State']


#1.Filter the column 'LDS Age Category' and make categories for Ages (<65,65-74,75+). 
#'LDS Age Category' for Age<65 = 1
#'LDS Age Category' for 65-74 = 2 & 3 
#'LDS Age Category' for 75+ = 4 & 5 & 6
#2. Group by State codes to count the number of people in each age category.

age_lessthan_65=pd.DataFrame(read_data.loc[read_data['LDS Age Category']==1].groupby('State Code from Claim (SSA)')['LDS Age Category'].count())
age_lessthan_65['State']=age_lessthan_65.index
age_lessthan_65.columns=['Ages < 65','State']

age_between_65to74=pd.DataFrame(read_data.loc[read_data['LDS Age Category'].isin([2,3])].groupby('State Code from Claim (SSA)')['LDS Age Category'].count())
age_between_65to74['State']=age_between_65to74.index
age_between_65to74.columns=['Ages 65-74','State']

age_greaterthan_75=pd.DataFrame(read_data.loc[read_data['LDS Age Category'].isin([4,5,6])].groupby('State Code from Claim (SSA)')['LDS Age Category'].count())
age_greaterthan_75['State']=age_greaterthan_75.index
age_greaterthan_75.columns=['Ages 75+','State']


#Merge all the dataframes on column 'State' 

final_output=pd.merge(pd.merge(pd.merge(pd.merge(females, males, on='State', how='outer'),age_lessthan_65,on='State', how='outer'),age_between_65to74,on='State', how='outer'),age_greaterthan_75,on='State', how='outer').fillna(0)

#Rearrange the order of columns for writing to csv file
column_list=final_output.columns.tolist()

cols=[column_list[1],column_list[0],column_list[2],column_list[3],column_list[4],column_list[5]]

final_output[cols].to_csv('output1.csv',index = False)


# If the output file with same name is already present replace it
try:
    final_output[cols].to_csv('output1.csv',index = False)   
except OSError:
    pass
    os.remove(filename)
    final_output[cols].to_csv('output1.csv',index = False)