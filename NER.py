import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

text = "Sachin Tendulkar was born in India and worked with Google."

doc = nlp(text)

# Named Entity Recognition
for ent in doc.ents:
    print(ent.text, "->", ent.label_)