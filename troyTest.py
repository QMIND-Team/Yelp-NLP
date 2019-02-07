'''
Troy's testing module for the webscraper
'''
import scrape as sc
import re
import numpy as np 
import pandas as pd

def addToRevs(revs, baseurl):
    '''Docstring
    Blah blah do stuff
    extends list then converts to pd
    returns pandas dataframe
    '''
    stop = False
    index = 0
    numrevs = -1

    while not stop:
        url = baseurl + "?start=" + str(index)
        page = sc.getPage(url)
        soup = sc.openSoup(page)

        # If we havent figured out yet, get the max number of reviews from the top of the page
        # Note: This lies!
        if numrevs == -1:
            maxes = soup.find_all('span', class_="review-count rating-qualifier")
            tmpstring = maxes[0].get_text()
            # This next line turns the string "64 reviews" into the int "64"
            numrevs = int(re.findall(r'\d+', tmpstring)[0]) #Yeah that could be broken to a few lines for readability

        lists = soup.find_all('div', class_="review-content")
        parlist = [l.find_all('p') for l in lists]

        pars = []
        for plist in parlist:
            for p in plist:
                pars.append(p)

        df = pd.DataFrame([p.get_text() for p in pars], columns = ["Reviews"]) #saves 20 reviews as dataframe
        revs = pd.concat([df,revs], ignore_index= True) #adds to our main dataframe, avoids index from repeatedly going 0-19

        index += 20

        if index >= numrevs:
            # Not sure if the best way is to do this, or to make this a break and have the while loop be an infinite loop.
            stop = True
    
    return revs

import pprint as pp

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
    revs = addToRevs(revs, url)

if __name__ == "__main__":
    main()