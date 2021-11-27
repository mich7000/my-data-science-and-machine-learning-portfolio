# <> first page contains application that predict whether a comment has positive / negative sentiment
# <> second page contains dashboard created from the predictions made on the test data.


import streamlit as st
import pandas as pd 
import numpy as np
from joblib import load

# loads saved model
model = load('output/model_tuned.pkl')


st.header('Project 4 - Sentiment Analysis on Product Reviews')

# create predictor function.
def predictor(text):
    output = model.predict([text])[0]

    if output == 1:
        sentiment= 'Positive review'
    else:
        sentiment = 'Negative review'

    return sentiment

# create interface function.
def main():
    
    st.write('*Please type or paste the review in the text box below.*')
    text = st.text_input('Review', 'type or paste review here.')
    result = ""
    
    if st.button('submit'):
        result = predictor(text)
        st.write('Sentiment')
        st.success(result)


if __name__ == "__main__":
    main()
