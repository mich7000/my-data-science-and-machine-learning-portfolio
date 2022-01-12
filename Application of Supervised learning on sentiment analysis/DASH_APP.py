
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# import the required libraries
import re
import numpy as np


# NLP tools
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.collocations import FreqDist, BigramCollocationFinder
#import text_normalizer as tn
import word_cloud as wc
import spacy
from spacy import displacy

stop_words = nltk.corpus.stopwords.words('english')


# data loading and cleaning
FILE='output_data.csv'
PATH='data/sentiment labelled sentences/amazon_cells_labelled.txt'

df = pd.read_csv(FILE)
amazon_cells= pd.read_csv(PATH,  delimiter='\t',header=None)
amazon_cells.columns = ['Review', 'Sentiment']
reviews_list= amazon_cells['Review'].to_list()

# tokenize the data
tokenizer = nltk.RegexpTokenizer(r"\w+")
token_list = []
for s in reviews_list:
    t = tokenizer.tokenize(s)
    t = [w.lower() for w in t ]
    token_list.extend(t)

filtered_sentence = [word for word in token_list if word not in stop_words]
wc.show_wordcloud(filtered_sentence, max_word=30)

# EDA
frame1, frame2= st.columns([12, 9])

with frame1: 
        # word cloud
        st.markdown("""<font size=6>Word cloud of the most frequent words</font>""", unsafe_allow_html=True)
        st.write("""It is clearly seen that the domain of the analysis is focused on tech products, 
                    Mostly focusing on smaller gadgets such as phones and its accessories.""")
        from wordcloud import WordCloud


        # Create some sample text
        text = ' ,'.join(filtered_sentence)

        # Create and generate a word cloud image:
        wordcloud = WordCloud(background_color='white', max_words=30).generate(text)

        # Display the generated image:
        f= plt.figure()
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot(f)

with frame2:
        # sentiment plot
        st.markdown("<font size=6>Sentiment Distribution.</font>", unsafe_allow_html=True)
        
        st.write("""There is vast gap between negative and positive sentiment, 
                    this indicates that most of the customers are very dissatisfied 
                    about the condition of the product they purchased. """)
        f = plt.figure()
        sns.countplot(df['label'])
        sns.despine()
        plt.xlabel('')
        plt.ylabel('')
        st.pyplot(f)






