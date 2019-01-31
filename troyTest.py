'''
Troy's testing module for the webscraper
'''
import scrape as sc
import re

def printReviews(reviews):
    '''Insert meaningful docstring here
    Blah Blah
    Should this code go at the top, bottom, or in scrape.py?
    Wait python is interpreted it can't go at the bottom.
    I think probably scrape.py, but more formalized maybe?
    This is sort of just a crap function as it is right now.
    There's really no need to 
    '''
    print(*reviews, sep="\n\n") # The * here sort of unpacks the list in a cool way.  I just learned it.
    print("\n", len(reviews))

def addToRevs(revs, baseurl):
    '''Docstring
    Blah blah do stuff
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

        revs.extend([p.get_text() for p in pars]) # Extend, not append here

        index += 20

        if index >= numrevs:
            # Not sure if the best way is to do this, or to make this a break and have the while loop be an infinite loop.
            stop = True
    
    return revs


def main():
    print("Let's go! \n") #Sanity check that things are starting
    url = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
    #url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
    revs = []

    revs = addToRevs(revs, url)
    printReviews(revs)

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