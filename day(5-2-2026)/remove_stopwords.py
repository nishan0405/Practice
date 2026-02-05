from nltk.corpus import stopwords
words=word_tokenize(story1)
stop_words=set(stopwords.words('english'))
filtered=[]
for word in words:
  if word.lower() not in stop_words:
    filtered.append(word)
print(filtered)