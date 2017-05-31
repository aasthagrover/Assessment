# Question 2-Extra Credit Question

#Function to read data from the csv file
def readFile():
    import os
    try:
        x = input()
        file=os.path.normpath(os.path.join(x, 'data.csv'))
        import pandas as pd
        read_data = pd.read_csv(file)
        return read_data
        pass
    except OSError:
        print("Path not valid. Please enter the path again")
        return readFile() # if error in reading file, ask for user input for filepath again .
    
    
def main():
    try:
        read_data = readFile()
        import pandas as pd
        # 1. Group the data by Claim utilization Day count
        # 2. Count the number of claims for each category of claim utilization day where  categories are made when Claim utilization days are same.
        # 3. Name the dataframe as 'total_claims_for_eachnumberof_utilization_day' which contains count of claims for each category of claim utilization day
        total_claims_for_eachnumberof_utilization_day = pd.DataFrame(read_data.groupby('Claim Utilization Day Count')['Claim number'].count())
        total_claims_for_eachnumberof_utilization_day['Utilization Range'] = total_claims_for_eachnumberof_utilization_day.index
        total_claims_for_eachnumberof_utilization_day.columns = ['Counts','Utilization Range']

        # Make a list of all the unique Claim Utilization days.
        all_utilization_day_ranges = []
        for r in range(1,max(total_claims_for_eachnumberof_utilization_day['Utilization Range'])+1):
            all_utilization_day_ranges.append(r)

        # Calculate the sum of all the claims for any number of the Claim Utilization days  
        total_sum_of_all_claims = total_claims_for_eachnumberof_utilization_day.loc[total_claims_for_eachnumberof_utilization_day['Utilization Range'].isin(all_utilization_day_ranges),'Counts'].sum()


        # Make a list 'sum_of_claims_over_each_utilization_range' which contains the sum of the number of claims for each individual Claim Utilization day range.
        sum_of_claims_over_each_utilization_range = []

        # The categories for Claim Utilization day range are as follows: 0,1,2,3,4,5,6-10,11,30, greater than equal to 30 days
        # for categories where claim utilization days are to be taken as(Example : [6-10], [11-30],[30 and above]). Make 3 lists to contain the range numbers 
        range6_10=[]
        range11_30=[]
        range30_plus=[]

        #append the count of number of claims for 0-5 claim utilization days in a list 'sum_of_claims_over_each_utilization_range'
        for value in range(0,6):
            sum_of_claims_over_each_utilization_range.append(total_claims_for_eachnumberof_utilization_day.loc[total_claims_for_eachnumberof_utilization_day['Utilization Range']==value,'Counts'].sum())

        for i in range(6,11):
            range6_10.append(i)

        for j in range(11,31):
            range11_30.append(j)

        for k in range(30,max(total_claims_for_eachnumberof_utilization_day['Utilization Range'])+1):
            range30_plus.append(k)

        #all_ranges list contains the lists for ranges of claim utilization days. Example: [6-10], [11-30],[30 and above]
        all_ranges=[range6_10,range11_30,range30_plus]

        #append the count of number of claims for [6-10],[11-30],[30 and above] claim utilization day ranges a list 'sum_of_claims_over_each_utilization_range'
        for item in all_ranges:
            sum_of_claims_over_each_utilization_range.append(total_claims_for_eachnumberof_utilization_day.loc[total_claims_for_eachnumberof_utilization_day['Utilization Range'].isin(item),'Counts'].sum())


        # Make a list 'percentage_list' which contains the percentages of claims in each category range of Claim Utilization Day.
        percentage_list=[]

        for i,count in enumerate(sum_of_claims_over_each_utilization_range):
            percentage_list.append((count*100)/total_sum_of_all_claims)


        # Make a dataframe which contains teh Claim Utilization Day Range, Count of claims for each Utilization Day Range, 
        # Percentage of Claims for each range
        final_frame=pd.DataFrame({'Utilization Range':["0","1","2","3","4","5","'6-10'","'11-30'","30 Plus"],'Counts':sum_of_claims_over_each_utilization_range,'Percentages':percentage_list})
        col=final_frame.columns.tolist()
        final_columns=[col[2],col[0],col[1]]
        
        # Handle the exception if file with the same name as 'output2' is already present in the directory. Replace the file with new file
        try:
            final_frame[final_columns].to_csv('output2.csv',index = False)   
        except OSError:
            pass
            os.remove(filename)
            final_frame[final_columns].to_csv('output2.csv',index = False)
    except:
        print("Unexpected Error")
        
        
#Execute the main function         
if __name__ == "__main__": main()