'''
Word cloud module.  Takes in a string and outputs a word cloud.
Looking to setup to take in a dataframe and cacatonate all the reviews for one large cloud.

Following for now:
https://www.datacamp.com/community/tutorials/wordcloud-python
'''
#probably don't need all of these...
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import scrape as sc 

import matplotlib.pyplot as plt

def createWordCloud(text):
    # Create and generate a word cloud image:
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
