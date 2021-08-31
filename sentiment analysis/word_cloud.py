

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)

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