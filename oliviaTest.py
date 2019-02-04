'''
Olivia's test to convert reviews to pandas
'''

import troyTest as tt

def main():
    #url = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
    url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
    
    revs = []

    revs = tt.addToRevs(revs, url)
    tt.printReviews(revs)
  
if __name__== "__main__":
  main()