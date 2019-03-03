import scrape as sc
import numpy as np
import keras
from keras.models import load_model
import pickle
from sklearn.feature_extraction.text import CountVectorizer

data = pickle.load(open("dfmid.p", "rb"))
vocab = pickle.load(open("vocab.p","rb"))

## Data Vectorization

# Below we will be vectorizing the Yelp reviews for the various credit unions. Please refer to Google Document for list of urls utilized in the collection of the Yelp Reviews. Will vectorize data, with 1- and 2- grams.

# Here we are importing a useful function that converts our data set of sentences into a large matrix of 0's and 1's.

# Set up the vectorizer and model that we've previously trained to get sentiment

vectorizer = CountVectorizer(binary=True, lowercase=False, vocabulary = vocab)
# 'binary=false' would make the matrix count the frequency of a word in the sentence, instead of just marking its presence
# for some reason this wasn't working unless lowercase=false, some problem with the cleaned data I suppose

model = load_model("sentiment_predictor.h5")

## Sentiment Prediction 

# Will now import the model we developed during our warm-up project for the purposes of predicting the sentiment of credit union reviews. This can be done now that we have cleaned and vectorized our data. Since keras is wonderful and has a built-in model prediction feature, won't unnecessarily complicate the prediction process by re-inventing the wheel. But rather, will simply pass in our new data into the built in prediction feature in keras.


def get_sentiment(review):
    singletonlist = [review]
    vectorraw = vectorizer.fit_transform(singletonlist)
    
    vector = vectorraw.todense()
    vector = np.asarray(vector)
    
    sentiment = model.predict(vector[0:1])[0][0]
    
    return sentiment


def addSentiments(revs):
    companies = list(revs.columns.levels[0])
    for company in companies:
        #iterate through each review
        for index, rev in revs[company, 'Reviews'].iterrows():
            #do sentiment analysis with rev
            sentiment = get_sentiment(rev)
            #place sentiment val in dataframe
            revs.loc[index, [(company, 'Sentiment')] = sentiment

    return revs

