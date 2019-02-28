'''
Webscraper module.  Everything we need to scrape the Yelp data, putting everything we want into a Pandas dataframe.

These functions should be imported by our main program.

Following for now:
https://www.dataquest.io/blog/web-scraping-tutorial-python/
'''
import requests
from bs4 import BeautifulSoup
import re
import numpy as np 
import pandas as pd

def getPage(url):
    ''' Get the page object
    Using the requests library.
    '''
    page = requests.get(url)
    return page

def openSoup(page):
    ''' Make the soup object.
    Takes a page object, preferably made by getPage().
    '''
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

# def addToRevsList(revs, baseurl):
#     ''' Add to the reviews, list version
#     Take in the reviews list and the base url to scrape
#     returns an extended reviews list, with the new reviews added
#     '''
#     stop = False
#     index = 0
#     numrevs = -1

#     while not stop:
#         url = baseurl + "?start=" + str(index)
#         page = getPage(url)
#         soup = openSoup(page)

#         # If we havent figured out yet, get the max number of reviews from the top of the page
#         # Note: This lies!
#         if numrevs == -1:
#             maxes = soup.find_all('span', class_="review-count rating-qualifier")
#             tmpstring = maxes[0].get_text()
#             # This next line turns the string "64 reviews" into the int "64"
#             numrevs = int(re.findall(r'\d+', tmpstring)[0]) #Yeah that could be broken to a few lines for readability

#         lists = soup.find_all('div', class_="review-content")
#         parlist = [l.find_all('p') for l in lists]

#         # parlist is a list of (single item) lists of p blocks
#         pars = []
#         for plist in parlist:
#             for p in plist:
#                 pars.append(p)

#         revs.extend([p.get_text() for p in pars]) # Extend, not append here

#         index += 20

#         if index >= numrevs:
#             # Not sure if the best way is to do this, or to make this a break and have the while loop be an infinite loop.
#             stop = True
    
#     return revs

def extractRevs(soup):
    '''TODO
    Docstring
    '''
    lists = soup.find_all('div', class_="review-content")
    parlist = [l.find_all('p') for l in lists]
    
    pars = []
    for plist in parlist:
        for p in plist:
            pars.append(p.get_text())

    return pars

def extractDates(soup):
    ''' TODO
    Docstring
    '''
    dates = soup.find_all('span', class_="rating-qualifier")
    datelistraw = [d.get_text().strip() for d in dates]

    for date in list(datelistraw):
        if "reviews" in date:
            datelistraw.remove(date)

    datelist = []

    for date in datelistraw:
        match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', date).group(0)
        datelist.append(match)
    
    return datelist

def addToRevs(revs, baseurl):
    '''Add to the reviews, dataframe version
    Take in the reviews list and the base url to scrape
    returns an extended reviews list, with the new reviews added
    '''
    stop = False
    index = 0
    numrevs = -1

    while not stop:
        url = baseurl + "?start=" + str(index)
        page = getPage(url)
        soup = openSoup(page)

        # If we havent figured out yet, get the max number of reviews from the top of the page
        # Note: This lies!
        if numrevs == -1:
            maxes = soup.find_all('span', class_="review-count rating-qualifier")
            tmpstring = maxes[0].get_text()
            # This next line turns the string "64 reviews" into the int "64"
            numrevs = int(re.findall(r'\d+', tmpstring)[0]) #Yeah that could be broken to a few lines for readability

        pars = extractRevs(soup)
        dates = extractDates(soup)

        #Possibilty that these aren't lined up properly. There are 2 more dates than revs for some reason??
        dfrevs = pd.DataFrame(data = pars, columns = ['Reviews']) #saves 20 reviews as dataframe
        dfdates = pd.DataFrame(data = dates, columns = ['Dates']) #saves 20 dates as dataframe
        df = dfrevs.join(dfdates) #merges revs and dates
        revs = pd.concat([df,revs], ignore_index= True, sort = True)  #adds to our main dataframe, avoids index from repeatedly going 0-19

        index += 20

        if index >= numrevs:
            # Not sure if the best way is to do this, or to make this a break and have the while loop be an infinite loop.
            stop = True
    
    return revs

def createRevs(baseurl):
    '''Creates a review dataframe with review, sentiment and url column.
    '''
    stop = False
    index = 0
    numrevs = -1

    col = ["Reviews","Sentiment", "Url"]
    revs = pd.DataFrame(columns = col)

    while not stop:
        url = baseurl + "?start=" + str(index)
        page = getPage(url)
        soup = openSoup(page)

        # If we havent figured out yet, get the max number of reviews from the top of the page
        # Note: This lies!
        if numrevs == -1:
            maxes = soup.find_all('span', class_="review-count rating-qualifier")
            tmpstring = maxes[0].get_text()
            # This next line turns the string "64 reviews" into the int "64"
            numrevs = int(re.findall(r'\d+', tmpstring)[0]) #Yeah that could be broken to a few lines for readability

        pars = extractRevs(soup)
        dates = extractDates(soup)

        #Possibilty that these aren't lined up properly. There are 2 more dates than revs for some reason??
        dfrevs = pd.DataFrame(data = pars, columns = ['Reviews']) #saves 20 reviews as dataframe
        dfdates = pd.DataFrame(data = dates, columns = ['Dates']) #saves 20 dates as dataframe
        df = dfrevs.join(dfdates) #merges revs and dates
        revs = pd.concat([df,revs], ignore_index= True, sort = True)  #adds to our main dataframe, avoids index from repeatedly going 0-19

        index += 20

        if index >= numrevs:
            # Not sure if the best way is to do this, or to make this a break and have the while loop be an infinite loop.
            stop = True
    
    return revs

def mergeRevs(revsList, companyList):
    '''
    Merges all reviews into one dataframe with multiindexing
    '''
    dfMerged = pd.concat(revsList, axis = 1, keys=companyList, names=['Company','Type'])
    return dfMerged

