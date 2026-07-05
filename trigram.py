import nltk
from nltk.util import trigrams

text = "I am learning natural language processing"

words = text.split()

# Generate trigrams
tri_grams = list(trigrams(words))

print("Trigrams:")
for tg in tri_grams:
    print(tg)