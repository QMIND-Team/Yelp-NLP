'''
Troy's testing module for the webscraper
'''
import scrape as sc
import pprint as pp

def main():
    print("Let's go! \n") #Sanity check that things are starting
    #url = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
    url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
    revs = []

    revs = sc.addToRevsList(revs, url)
    pp.pprint(revs)

if __name__ == "__main__":
    main()