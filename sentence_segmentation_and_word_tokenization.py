import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# nltk.download('punkt')

text = "Hello everyone. Welcome to NLP practicals. Tokenization is important."

# Sentence Segmentation
sentences = sent_tokenize(text)
print("Sentences:")
print(sentences)

# Word Tokenization
words = word_tokenize(text)
print("\nWords:")
print(words)