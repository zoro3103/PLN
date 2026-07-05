from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

text = """
Artificial Intelligence is transforming the world.
It helps machines learn from data and make decisions.
AI is used in healthcare, education, and business.
It improves efficiency and reduces human effort.
"""

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()

print("Summary:")
for sentence in summarizer(parser.document, 2):
    print(sentence)