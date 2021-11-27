import nltk
import pandas as pd
import matplotlib.pyplot as plt
import spacy
from spacy import displacy

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)

# plots out word cloud of most frequent words
def show_wordcloud(token, title = None, max_word= 5):
    # genrate words
    wordcloud = WordCloud(background_color='white', stopwords=stopwords,  max_words= max_word, max_font_size=40,   scale=3,  random_state=1).generate(str(token))
    # make a plot
    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()


# display named entity in a text..
def display_named_entity(text):
    """
    The function displays text with named entity tag attached to it.
    text: str, must be raw text. 
    """

    nlp = spacy.load("en_core_web_sm")
    nlp_text = sp(text)
    output = displacy.render(nlp_text, style='ent', jupyter=True) 
    
    return output


# plots the most frequent words
def most_common_plot(token, n=0):
    """
    Plots the most common n words
    token: list (array-like), iterable
    """
    most_common = FreqDist(word for word in token)
    out = pd.Series(dict(most_common)).\
    sort_values(ascending=False)[:n].\
    plot(kind='barh', figsize=(5, 7), title='Most common words')
    
    return out

# finds the collocation of words
def show_collocations(token, n):
    """
    Prints outs data frame of collocations and the scores...
    """
    bgm    = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(token)
    scored = finder.score_ngrams( bgm.likelihood_ratio  )
    collocations = pd.DataFrame(scored)
    collocations.columns = ['collocation', 'score']
    collocations.set_index('collocation', inplace=True)

    out0 = collections.head(n)
    return out0

## computes the compound of a sentiment.
## normally used to compare the polarity of different corpus.
def compound(x, alpha=15):
    
    score= x/np.sqrt(x**2+alpha)
    return score
