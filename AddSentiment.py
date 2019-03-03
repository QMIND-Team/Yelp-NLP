import scrape as sc
import numpy as np
import keras
from keras.models import load_model
import pickle

data = pickle.load(open("dfmid.p", "rb"))
vocab = pickle.load(open("vocab.p","rb"))