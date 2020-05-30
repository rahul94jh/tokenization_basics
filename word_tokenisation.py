from nltk import word_tokenize

# import nltk
# nltk.download("punkt")

""" https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html
https://medium.com/data-science-in-your-pocket/tokenization-algorithms-in-natural-language-processing-nlp-1fceab8454af """

document = """At nine o'clock I visited him myself. It looks like religious mania, and he'll 
soon think that he himself is God."""


# tokenising on space using string split function
print(document.split())

# tokenising using nltk word tokeniser
words = word_tokenize(document)
print(words)

"""NLTK's word tokeniser not only breaks on whitespaces but also breaks contraction words such as he'll into "he" and "'ll".
 On the other hand it doesn't break "o'clock" and treats it as a separate token."""
