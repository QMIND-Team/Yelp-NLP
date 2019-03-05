import numpy as np 
import pandas as pd 
import pickle
import math

data = pickle.load(open("dfFinal.p", "rb"))

companies = list(data.columns.levels[0])
sentAves = pd.DataFrame(columns = companies)

years = range(2008, 2020)

#go through each company
for company in companies:
    cdata = data[company]

    #drop rows without dates
    cdata = cdata.dropna(subset=['Dates'])
    #convert Dates column to type datetime 
    cdata['Dates'] = pd.to_datetime(cdata['Dates'])
    #sort reviews in ascending order by date, not sure if necessary
    cdata = cdata.sort_values(by =['Dates'])

    #create dataframe to place each sentiment average
    sentimentdf = pd.DataFrame(index = years, columns = [company])

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
            sentimentdf.at[year, company] = 0.5
        else:
            sentimentdf.at[year, company] = yearAve

    print(sentimentdf)


'''

#go through each review
    for row in cdata.itertuples():
        #print(row.Dates)
        #grab year, sentiment values
        cyear = row.Dates.year
        sentiment = pd.Series(row.Sentiment)
        #place sentiment in dataframe
        sentimentdf[year] = sentimentdf[year].append(sentiment, ignore_index = True)
        sentimentdf[year] = sentimentdf[year].append(sentiment, ignore_index = True)
    for year in years:
        if (data[company, 'Dates'].year == year):
            print(data[company, 'Dates'])
        #    yearSent = data[company].dt.year

       # print(company + "\n" + yearSent)
    
    #find the average sentiment of that year

    #save to spreadsheet of data to be added to other dataframe
'''
