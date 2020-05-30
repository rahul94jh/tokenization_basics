from nltk import sent_tokenize

document = "At nine o'clock I visited him myself. It looks like religious mania, and he'll \
soon think that he himself is God."

# Tokenising based on sentence requires you to split on the period ('.').
#  Let's use nltk sentence tokeniser.
sentence = sent_tokenize(document)
print(sentence)
