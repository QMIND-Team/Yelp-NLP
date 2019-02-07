'''
Troy's testing module for the webscraper
'''
import scrape as sc

'''
Not needed anymore?

def printReviews(reviews):
    Insert meaningful docstring here
    Blah Blah
    Should this code go at the top, bottom, or in scrape.py?
    Wait python is interpreted it can't go at the bottom.
    I think probably scrape.py, but more formalized maybe?
    This is sort of just a crap function as it is right now.
    There's really no need to 
    
    print(*reviews, sep="\n\n") # The * here sort of unpacks the list in a cool way.  I just learned it.
    print("\n", len(reviews))
'''

def main():
    print("Let's go! \n") #Sanity check that things are starting
    #url = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
    url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
    revs = []

    revs = sc.addToRevsList(revs, url)
    print(revs, len(revs))

if __name__ == "__main__":
    main()

'''
Conclusion:
This sort of works!  
TODO:
* Make revs a pandas object.  (Should this be rewritten as pandas all the way though or should it just be converted at the end?)
* Integrate this into a larger program and make sure it works.  It should be able to be run with just `revs = addToRevs(revs, url)`
* Maybe make it work with whatever our "big pandas table/database" will be
'''