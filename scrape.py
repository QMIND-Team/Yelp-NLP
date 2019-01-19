'''
Webscraper module.  Everything we need to scrape the Yelp data, putting everything we want into a Pandas dataframe.

These functions should be imported by our main program.

Following for now:
https://www.dataquest.io/blog/web-scraping-tutorial-python/
'''
import requests
from bs4 import BeautifulSoup

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


