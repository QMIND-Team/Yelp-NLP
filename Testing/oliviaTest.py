'''
Olivia's test to convert reviews to pandas
'''

import numpy as np
import pandas as pd 

import sys
sys.path.append("..")
import scrape as sc
import TextClusteringLSA as tc

def listToPd (list):
  
  df = pd.DataFrame(list)

  return df


def main():
  url1 = "https://www.yelp.ca/biz/meridian-credit-union-toronto-4"
  url2 = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"

  rev1 = sc.createRevs(url2)
  rev2 = sc.createRevs(url2)
  revs = sc.mergeRevs([rev1, rev2], ['Harpers', 'CU'])
    
  tc.generateTopics(revs, 'Harpers', 3)

  
if __name__== "__main__":
  main()