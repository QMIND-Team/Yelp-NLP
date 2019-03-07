import numpy as np 
import pandas as pd 
import pickle
import math

data = pickle.load(open("dfFinal.p", "rb"))

years = range(2005, 2020)

def getSentimentAves(company):
    #grab company's columns
    cdata = data[company]

    #drop rows without dates
    cdata = cdata.dropna(subset=['Dates'])
    #convert Dates column to type datetime 
    cdata['Dates'] = pd.to_datetime(cdata['Dates'])
    #sort reviews in ascending order by date, not sure if necessary
    cdata = cdata.sort_values(by =['Dates'])

    #create dataframe to place each sentiment average
    sentAves = pd.DataFrame(index = years, columns = ['Average Sentiment'])

    for year in years:
        #grab all sentiments for the year
        yearSent = cdata.loc[cdata['Dates'].dt.year == year]
        yearSent = yearSent['Sentiment'].reset_index().drop('index', axis = 1)
        #get average sentiment for the year
        numSent = yearSent['Sentiment'].count()
        sumSent = yearSent['Sentiment'].sum()
        yearAve = sumSent / numSent
        #place average in df
        if (math.isnan(yearAve)):
            sentAves.at[year] = 0.5
        else:
            sentAves.at[year] = yearAve

    return sentAves
