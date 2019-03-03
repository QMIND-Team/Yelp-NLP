'''
Troy's testing module for the webscraper
'''
import scrape as sc
import pandas as pd
import pickle
import wordCloud as wc

# From scrape.py

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


# def addToRevs(revs, baseurl):
#     '''Add to the reviews, dataframe version
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

#         pars = extractRevs(soup)
#         dates = extractDates(soup)

#         #Possibilty that these aren't lined up properly. There are 2 more dates than revs for some reason??
#         dfrevs = pd.DataFrame(data = pars, columns = ['Reviews']) #saves 20 reviews as dataframe
#         dfdates = pd.DataFrame(data = dates, columns = ['Dates']) #saves 20 dates as dataframe
#         df = dfrevs.join(dfdates) #merges revs and dates
#         revs = pd.concat([df,revs], ignore_index= True, sort = True)  #adds to our main dataframe, avoids index from repeatedly going 0-19

#         index += 20

#         if index >= numrevs:
#             # Not sure if the best way is to do this, or to make this a break and have the while loop be an infinite loop.
#             stop = True
    
#     return revs

urllist = ['https://www.yelp.ca/biz/vancity-credit-union-vancouver-4'
, 'https://www.yelp.ca/biz/vancity-credit-union-vancouver-8'
, 'https://www.yelp.ca/biz/vancity-vancouver-6'
, 'https://www.yelp.ca/biz/vancity-vancouver-5'
, 'https://www.yelp.ca/biz/vancity-burnaby-2'
, 'https://www.yelp.ca/biz/vancity-savings-credit-union-vancouver-5'
, 'https://www.yelp.ca/biz/vancity-burnaby-3'
, 'https://www.yelp.ca/biz/vancity-burnaby-4'
, 'https://www.yelp.ca/biz/vancity-savings-credit-union-vancouver-4'
, 'https://www.yelp.ca/biz/vancity-vancouver-2'
, 'https://www.yelp.ca/biz/vancity-richmond'
, 'https://www.yelp.ca/biz/vancity-vancouver'
, 'https://www.yelp.ca/biz/vancity-surrey'
, 'https://www.yelp.ca/biz/vancity-credit-union-vancouver-9'
, 'https://www.yelp.ca/biz/vancity-vancouver-3'
, 'https://www.yelp.ca/biz/vancity-savings-surrey'
, 'https://www.yelp.ca/biz/vancity-coquitlam'
, 'https://www.yelp.com/biz/vancity-credit-union-vancouver-4?rh_ident=banking_fee&rh_type=phrase'
, 'https://www.yelp.ca/biz/coast-capital-savings-vancouver-3'
, 'https://www.yelp.ca/biz/coast-capital-savings-vancouver-2'
, 'https://www.yelp.ca/biz/coast-capital-savings-victoria-2'
, 'https://www.yelp.ca/biz/coast-capital-savings-richmond-4'
, 'https://www.yelp.ca/biz/coast-capital-savings-surrey-3'
, 'https://www.yelp.ca/biz/coast-capital-savings-coquitlam'
, 'https://www.yelp.ca/biz/coast-capital-savings-richmond-5'
, 'https://www.yelp.ca/biz/coast-capital-savings-vancouver'
, 'https://www.yelp.ca/biz/coast-capital-savings-duncan'
, 'https://www.yelp.ca/biz/coast-capital-savings-pitt-meadows'
, 'https://www.yelp.ca/biz/coast-capital-savings-langley'
, 'https://www.yelp.ca/biz/coast-capital-savings-burnaby'
, 'https://www.yelp.ca/biz/servus-credit-union-edmonton-15'
, 'https://www.yelp.ca/biz/servus-credit-union-edmonton-3'
, 'https://www.yelp.ca/biz/servus-credit-union-edmonton-6'
, 'https://www.yelp.ca/biz/servus-credit-union-edmonton-25'
, 'https://www.yelp.ca/biz/servus-credit-union-calgary-2'
, 'https://www.yelp.ca/biz/servus-credit-union-edmonton-23'
, 'https://www.yelp.ca/biz/servus-credit-union-edmonton-21'
, 'https://www.yelp.ca/biz/servus-credit-union-sherwood-park'
, 'https://www.yelp.ca/biz/servus-credit-union-edmonton-5'
, 'https://www.yelp.ca/biz/servus-credit-union-fort-saskatchewan'
, 'https://www.yelp.com/biz/servus-credit-union-place-saint-albert?page_src=related_bizes&hrid=i91_gzhlekM3s6zAi72Rvg&rh_ident=indoor_playground&rh_type=phrase'
, 'https://www.yelp.ca/biz/meridian-credit-union-toronto-4'
, 'https://www.yelp.ca/biz/meridian-credit-union-toronto'
, 'https://www.yelp.ca/biz/meridian-credit-union-pickering'
, 'https://www.yelp.ca/biz/meridian-credit-union-limited-etobicoke'
, 'https://www.yelp.com/biz/affinity-federal-credit-union-piscataway-2'
, 'https://www.yelp.ca/biz/affinity-credit-union-des-moines'
, 'https://www.yelp.ca/biz/affinity-federal-credit-union-hillsborough'
, 'https://www.yelp.ca/biz/affinity-plus-federal-credit-union-minneapolis'
, 'https://www.yelp.ca/biz/affinity-plus-federal-credit-union-saint-paul-4'
, 'https://www.yelp.ca/biz/affinity-federal-credit-union-middletown'
, 'https://www.yelp.ca/biz/affinity-federal-credit-union-new-brunswick'
, 'https://www.yelp.com/biz/affinity-plus-federal-credit-union-minneapolis-3'
, 'https://www.yelp.com/biz/affinity-federal-credit-union-morristown'
, 'https://www.yelp.ca/biz/assiniboine-credit-union-winnipeg-16'
]

namesraw = ['Vancity', 'Vancity', 'Vancity', 'Vancity', 'Vancity', 
'Vancity', 'Vancity', 'Vancity', 'Vancity', 'Vancity', 'Vancity', 'Vancity',
 'Vancity', 'Vancity', 'Vancity', 'Vancity', 'Vancity', 'Vancity',
  'Coast Capital Savings', 'Coast Capital Savings', 'Coast Capital Savings',
   'Coast Capital Savings', 'Coast Capital Savings', 'Coast Capital Savings',
    'Coast Capital Savings', 'Coast Capital Savings', 'Coast Capital Savings',
     'Coast Capital Savings', 'Coast Capital Savings', 'Coast Capital Savings', 
     'Servus Credit Union', 'Servus Credit Union', 'Servus Credit Union', 
     'Servus Credit Union', 'Servus Credit Union', 'Servus Credit Union', 
     'Servus Credit Union', 'Servus Credit Union', 'Servus Credit Union', 
     'Servus Credit Union', 'Servus Credit Union', 'Meridian Credit Union', 
     'Meridian Credit Union', 'Meridian Credit Union', 'Meridian Credit Union',
     'Affinity Federal Credit Union', 
     'Affinity Federal Credit Union', 'Affinity Federal Credit Union', 
     'Affinity Federal Credit Union', 'Affinity Federal Credit Union',
     'Affinity Federal Credit Union', 'Affinity Federal Credit Union', 
     'Affinity Federal Credit Union', 'Affinity Federal Credit Union', 
     'Assiniboine Credit Union'
     ]

#urllist = ["https://www.yelp.ca/biz/harpers-burger-bar-kingston", "https://www.yelp.ca/biz/meridian-credit-union-toronto-4","https://www.yelp.ca/biz/meridian-credit-union-toronto-4","https://www.yelp.ca/biz/meridian-credit-union-toronto-4","https://www.yelp.ca/biz/meridian-credit-union-toronto-4"]
revslistraw = []
revslist = []
#namesraw = ['Harpers', 'CU', 'CU', 'CU', 'CU']
names = []


def main():
    # Initial checks and configurations 
    if (len(urllist) != len(namesraw)):
        raise Exception("urllist and namesraw are misaligned!")
    pd.options.display.max_columns = 50
    print("Let's go! \n") #Sanity check that things are starting

    for url in urllist:
        print(url)
        revstmp = sc.createRevs(url)
        revslistraw.append(revstmp)
    
    # A tad hacky.  j indexes the revslist
    j = -1
    for i in range(0,len(namesraw)):
        if not(namesraw[i] in names):
            revslist.append(revslistraw[i])
            j += 1
            names.append(namesraw[i])
        else:
            revtmp = pd.concat([revslist[j],revslistraw[i]], ignore_index=True)
            revslist[j] = revtmp

    revs = sc.mergeRevs(revslist, names)

    print(revs)
    pickle.dump(revs, open("df.p","wb"))

    #Testing wordCloud
    #wc.createWordCloud(revs)

if __name__ == "__main__":
    main()