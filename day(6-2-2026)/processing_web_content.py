import nltk
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.util import bigrams

nltk.download("punkt")
url = "https://www.gutenberg.org/files/2554/2554-0.txt"
html = requests.get(url).text
raw = BeautifulSoup(html, "html.parser").get_text()
tokens = word_tokenize(raw)
text = Text(tokens)
text.concordance("the", lines=5)
text.collocations()
text.similar("man")
bg = list(bigrams(tokens))
print("\nFirst 10 bigrams:")
print(bg[:10])
