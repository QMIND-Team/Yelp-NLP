'''
Troy's testing module for the webscraper
'''
import scrape as sc
import pprint as pp
import pandas as pd
import wordCloud as wc 

def main():
    print("Let's go! \n") #Sanity check that things are starting
    #url = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
    url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
    revs = pd.DataFrame(columns=["Reviews", "Dates"])

    revs = sc.addToRevs(revs, url)
    print(revs)
    #pp.pprint(revs)

    #Testing wordCloud
    wc.createWordCloud(revs)

if __name__ == "__main__":
    main()