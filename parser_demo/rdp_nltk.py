from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP VP | NP
NP -> DT N | DT JJ N | DT JJ JJ N | PRP N | N
VP -> V | NP V | V RB | V RB PP | V NP | RB V | RB V NP | V RB
PP -> P NP
DT -> 'the' | 'a'
N -> 'dog' | 'chair' | 'back' | 'somebody' | 'coffee'
PRP -> 'his'
V -> 'slept' | 'stretched' | 'made'
P -> 'in' | 'by'
JJ -> 'cheerful' | 'black' | 'sleepy' | 'yellow'
RB -> 'quietly' | 'downstairs'
""")


# Create function to recursively parse sentence using custom grammar rules
def get_rd_parse(my_grammar, my_sentence):
    rd = RecursiveDescentParser(my_grammar)  # Create RD parser
    # rd.trace(3)  # Debugging
    processed_sent = my_sentence.lower().split()  # Conv string to lower & split into tokens
    return rd.parse(processed_sent)  # Return parse


# Create sentences
sentences = [
    "The cheerful black dog slept quietly by the chair",
    "A sleepy yellow dog stretched his back",
    "Somebody downstairs made coffee"
]
# Parse sentences & display results
for i, sent in enumerate(sentences):
    print("-"*40 + "\nSentence #{}".format(i + 1))
    for node in get_rd_parse(grammar, sent):
        print(node)