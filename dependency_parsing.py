import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

text = "The cat chased the mouse."

doc = nlp(text)

# Dependency Parsing
for token in doc:
    print(token.text, "->", token.dep_, "->", token.head.text)