import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')

words = ["running", "studies", "playing", "better"]

# Stemming
stemmer = PorterStemmer()
print("Stemming:")
for word in words:
    print(word, "->", stemmer.stem(word))

# Lemmatization
lemmatizer = WordNetLemmatizer()
print("\nLemmatization:")
for word in words:
    print(word, "->", lemmatizer.lemmatize(word))