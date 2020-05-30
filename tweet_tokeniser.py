from nltk import TweetTokenizer
from nltk import word_tokenize


message = "i recently watched this show called mindhunters:). \
i totally loved it 😍. it was gr8 <3. #bingewatching #nothingtodo 😎"

"""A problem with word tokeniser is that it fails to tokeniser emojis and other complex special characters such as word with hashtags.
 Emojis are common these days and people use them all the time."""

print(word_tokenize(message))

"""The word tokeniser breaks the emoji '<3' into '<' and '3' which is something that we don't want. 
Emojis have their own significance in areas like sentiment analysis where a happy face and sad face 
can salone prove to be a really good predictor of the sentiment. Similarly, the hashtags are broken 
into two tokens. A hashtag is used for searching specific topics or photos in social media apps such 
as Instagram and facebook. So there, you want to use the hashtag as is."""

# Let's use the tweet tokeniser of nltk to tokenise this message.
tokenizer = TweetTokenizer()
print(tokenizer.tokenize(message))

""" As you can see, it handles all the emojis and the hashtags pretty well. """
