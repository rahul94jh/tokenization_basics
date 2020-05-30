import os
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk import word_tokenize

""" Reading the text file """
# Open the file with read only permit
f = open("SMSSpamCollection.txt", "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
text = f.readlines()
# close the file after reading the lines.
f.close()

text = " ".join(text)
# replace tab
text = text.replace("\t", " ")
# print(text)

# create regex pattern to extract sms type and messages from each sms example we have
pattern = re.compile("(ham|spam)(.+)", flags=re.IGNORECASE | re.MULTILINE)
sms_data = pattern.findall(text)

# Let's see how many message collection we have
print(len(sms_data))

# create DataFrame using sms data
df = pd.DataFrame(sms_data, columns=["sms_type", "message"])


def func(variable):
    return False if variable in stopwords.words("english") else True


def tokenize_remove_stopwords(row):
    message = row.message
    message = word_tokenize(message)
    message_filtered = list(filter(func, message))
    return message_filtered


# Remove stop words and tokenize each message using nltk helper methods
df = df.apply(lambda x: tokenize_remove_stopwords(x), axis=1)

# print top 10 messages
print(df.head())
