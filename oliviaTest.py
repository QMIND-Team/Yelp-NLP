'''
Olivia's test to convert reviews to pandas
'''

import troyTest as tt
import numpy as np
import pandas as pd 

def listToPd (list):
  
  df = pd.DataFrame(list)

  return df


def main():
    #url = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
    url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
    
    revs = []

    revs = tt.addToRevs(revs, url)

    df = pd.DataFrame(revs)
    print(df)
    #tt.printReviews(revs)
  
if __name__== "__main__":
  main()