import pandas as pd
import numpy as np
import pickle

from sklearn.feature_extraction.text import CountVectorizer

import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


# Load the model
with open('./model/spam_filter_LR.pkl', 'rb') as file:
    model = pickle.load(file)
    
    
def normalize_text(text):
    # tokenize 
    result = word_tokenize(text)
    
    #lowercase
    result2 = [word.lower() for word in result]
    
    # remove punctuation
    result3 = [ word for word in result2 if word.isalpha()]

    # remove stopwords
    stp_word = set(stopwords.words('english') + ['subject'])
    result4 = [word for word in result3 if word not in stp_word]
    
    stemmer = PorterStemmer()
    result5 = [stemmer.stem(word) for word in result4]
    
    return result5

arr = open("./words.txt","r").read().split("\n")

def filter_words(words, arr):
    new_arr = []
    new_arr = [word for word in words if word in arr]
    
    # find the index of the words in the array
    index = []
    for word in new_arr:
        index.append(arr.index(word))
    
    
    unique = np.unique(index)    
    all_coff = []
    
    
    for i in unique:
        cnt = 0
        for j in index:
            if i == j:
                cnt += 1
        all_coff.append([i, cnt])
    
    return all_coff

def generate_vec(filter_words_arr):
    vec = np.zeros(len(arr))
    for word in filter_words_arr:
        vec[word[0]] = word[1]
    return vec

def predict(text):
    text = normalize_text(text)
    filter_words_arr = filter_words(text, arr)
    vec = generate_vec(filter_words_arr)
    return model.predict([vec])[0]

def predict_proba(text):
    text = normalize_text(text)
    filter_words_arr = filter_words(text, arr)
    vec = generate_vec(filter_words_arr)
    return model.predict_proba([vec])[0]

