import numpy as np 
import pandas as pd
import scrape as sc


url1 = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
url2 = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
revs1 = pd.DataFrame(columns=["Reviews"])
revs2 = pd.DataFrame(columns=["Reviews"])

revs1 = sc.addToRevs(revs1, url1)
revs2 = sc.addToRevs(revs2, url2)

col = ["Reviews","Sentiment" , "Url"]
df = pd.DataFrame(columns = col)

#df = pd.concat([df,revs], ignore_index= True)
df = pd.concat([revs1, revs2], keys=['Harpers', 'Credit Union'], names=['Company', 'Index'])
print(df)