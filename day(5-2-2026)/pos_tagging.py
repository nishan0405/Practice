import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
words=word_tokenize(story1)
tags=nltk.pos_tag(words)
tags