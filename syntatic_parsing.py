import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'mouse'
V -> 'chased'
""")

# Parser
parser = ChartParser(grammar)

sentence = "the cat chased the mouse".split()

for tree in parser.parse(sentence):
    print(tree)