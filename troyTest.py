'''
Troy's testing module for the webscraper
'''
import scrape as sc
import pprint as pp
import pandas as pd
import pickle
import wordCloud as wc 


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
, 'https://www.yelp.ca/biz/meridian-credit-union-limited-etobicoke']

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
     'Meridian Credit Union', 'Meridian Credit Union', 'Meridian Credit Union']


#urllist = ["https://www.yelp.ca/biz/harpers-burger-bar-kingston", "https://www.yelp.ca/biz/meridian-credit-union-toronto-4","https://www.yelp.ca/biz/meridian-credit-union-toronto-4","https://www.yelp.ca/biz/meridian-credit-union-toronto-4","https://www.yelp.ca/biz/meridian-credit-union-toronto-4"]
revslistraw = []
revslist = []
#namesraw = ['Harpers', 'CU', 'CU', 'CU', 'CU']
names = []


def main():
    if (len(urllist) != len(namesraw)):
        raise Exception("urllist and namesraw are misaligned!")

    pd.options.display.max_columns = 50
    print("Let's go! \n") #Sanity check that things are starting
    
    for url in urllist:
        print(url)
        revstmp = sc.createRevs(url)
        revslistraw.append(revstmp)
    
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
    pp.print(revs)
    pickle.dump(revs, open("df.p","wb"))

    #Testing wordCloud
    #wc.createWordCloud(revs)

if __name__ == "__main__":
    main()