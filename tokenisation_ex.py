""" Write a piece of code that breaks a given sentence into words and stores them in a list. 
Then remove the stop words from this list and then print the length of the list. 
Again, use the NLTK tokeniser to do this.

Sample input: “Education is the most powerful weapon that you can use to change the world” 
Expected output: 6 """


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


sentence = "Education is the most powerful weapon that you can use to change the world"

# change sentence to lowercase
sentence = sentence.lower()

# tokenise sentence into words
words = word_tokenize(sentence)

# extract nltk stop word list
stopwords = stopwords.words("english")


def func(variable):
    return False if variable in stopwords else True


# remove stop words
no_stops = list(filter(func, words))

# print length - don't change the following piece of code
print(len(no_stops))
