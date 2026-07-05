import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The cat is sleeping on the mat"

words = word_tokenize(text)
tags = pos_tag(words)

print(tags)