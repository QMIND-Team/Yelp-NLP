'''
Troy's testing module for the webscraper
'''
import scrape as sc
import pprint as pp
import pandas as pd

def main():
    print("Let's go! \n") #Sanity check that things are starting
    #url = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
    url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
    revs = pd.DataFrame(columns=["Reviews"])

    '''
    # Old way
    revs = sc.addToRevsList(revs, url)
    pp.pprint(revs)
    '''
    revs = sc.addToRevs(revs, url)
    pp.pprint(revs)

if __name__ == "__main__":
    main()