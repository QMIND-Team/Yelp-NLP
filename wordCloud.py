import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import scrape as sc 

import matplotlib.pyplot as plt

#bring in a review set
url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
revs = pd.DataFrame(columns=["Reviews", "Dates"]) 
revs = sc.addToRevs(revs, url)

# Start with one review:
text = revs.Reviews[0]

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()