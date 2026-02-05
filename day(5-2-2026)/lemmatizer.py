import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer=WordNetLemmatizer()
words=word_tokenize(story1)
lemma=[lemmatizer.lemmatize(word) for word in words]
lemma