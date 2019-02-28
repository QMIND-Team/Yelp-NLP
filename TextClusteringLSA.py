import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_colwidth", 200)

import scrape as sc 

url = "https://www.yelp.ca/biz/harpers-burger-bar-kingston"
revs = pd.DataFrame(columns=["Reviews", "Dates"])
revs = sc.addToRevs(revs, url)

# removing everything except alphabets`
revs['clean_revs'] = revs['Reviews'].str.replace("[^a-zA-Z#]", " ")

# removing short words
revs['clean_revs'] = revs['clean_revs'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))

# make all text lowercase
revs['clean_revs'] = revs['clean_revs'].apply(lambda x: x.lower())


from nltk.corpus import stopwords
stop_words = stopwords.words('english')

# tokenization
tokenized_doc = revs['clean_revs'].apply(lambda x: x.split()) 

# remove stop-words
tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in stop_words])

# de-tokenization
detokenized_doc = []
for i in range(len(revs)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)
    
revs['clean_revs'] = detokenized_doc

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', 
                             max_features= 1000, # keep top 1000 terms 
                             max_df = 0.5, 
                             smooth_idf=True)

X = vectorizer.fit_transform(revs['clean_revs'])

X.shape # check shape of the document-term matrix

from sklearn.decomposition import TruncatedSVD

# SVD represent documents and terms in vectors 
svd_model = TruncatedSVD(n_components=20, algorithm='randomized', n_iter=100, random_state=122)

svd_model.fit(X)

len(svd_model.components_)

terms = vectorizer.get_feature_names()

for i, comp in enumerate(svd_model.components_):
    terms_comp = zip(terms, comp)
    sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
    print("Topic "+str(i)+": ")
    for t in sorted_terms:
        print(t[0])
    print(" ")
