punctuation_filter=[]
for word in filtered:
  if word.isalnum():
    punctuation_filter.append(word)
print(punctuation_filter)