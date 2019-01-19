'''
Troy's testing module for the webscraper
'''
import scrape as sc

#url = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
page = sc.getPage(url)
soup = sc.openSoup(page)

lists = soup.find_all('div', class_="review-content")
parlist = [l.find_all('p') for l in lists]

pars = []
for plist in parlist:
    for p in plist:
        pars.append(p)

pars = [p.get_text() for p in list(pars)]

print(len(pars))

print(*pars, sep="\n\n")

'''Observation:
It only grabs the first 20 reviews.
The site has ?start=## to start at a later index of reviews.
If you try a URL past the max index it will give you "page 6 out of 5" on the bottom, and it will say there are no review found (or something of the sort)
'''