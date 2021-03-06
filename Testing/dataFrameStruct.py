import numpy as np 
import pandas as pd
import scrape as sc

url1 = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
url2 = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"

col = ["Reviews","Sentiment", "Url"]

revs1 = pd.DataFrame(columns = col)
revs2 = pd.DataFrame(columns = col)

revs1 = sc.addToRevs(revs1, url1)
revs2 = sc.addToRevs(revs2, url2)


#Companies and rev # on side, Reviews on top
df = pd.concat([revs1, revs2], keys=['Harpers', 'Credit Union'], names=['Company', 'Index'])
print(df)

#Companies and sections on top USING THIS FOR NOW
dfRaw = pd.concat([revs1, revs2], axis = 1, keys=['Harpers', 'Credit Union'], names=['Company','Type'])
print(dfRaw)

category = ["Average Star", "Average Rating", "Anwnual Growth"]
data = [[1,2], [3,4],[5,6]]
dfSummary = pd.DataFrame(data = data, index = category, columns = ['Harpers', 'Credit Union'])
print(dfSummary)