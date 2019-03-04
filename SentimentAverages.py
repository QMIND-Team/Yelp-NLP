import numpy as np 
import pandas as pd 
import pickle

data = pickle.load(open("dfFinal.p", "rb"))

print(data)

companies = list(data.columns.levels[0])

#go through each company
for company in companies:
    #sort reviews by year

    #find the average sentiment of that year

    #save to spreadsheet of data to be added to other dataframe
