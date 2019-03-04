import numpy as np 
import pandas as pd 
import pickle

data = pickle.load(open("dfFinal.p", "rb"))

print(data)

companies = list(data.columns.levels[0])

sentAves = pd.DataFrame(columns = companies)
#print(sentAves)

#go through each company
for company in companies:
    #convert Dates column to type datetime 
    data[company,'Dates'] = pd.to_datetime(data[company,'Dates'])
    #sort reviews in ascending order by date
    data[company] = data[company].sort_values(by =['Dates']))

    

    years = []
    #for year in years

    #find the average sentiment of that year

    #save to spreadsheet of data to be added to other dataframe
