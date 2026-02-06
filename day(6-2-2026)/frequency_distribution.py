import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
words=word_tokenize(story1)
fdist1 = FreqDist(words)