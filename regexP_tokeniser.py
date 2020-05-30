from nltk import regexp_tokenize

"""
There is a tokeniser that takes a regular expression and tokenises and returns result based on the pattern of regular expression."""

message = "i recently watched this show called mindhunters:). i totally loved it 😍. it was gr8 <3. #bingewatching #nothingtodo 😎"
# Pattern to extract each word starting with # i.e we are intrested in knowing the hastag's only
pattern = r"#[\w]+"

# Let's look at how we can use regular expression tokeniser.
print(regexp_tokenize(message, pattern))
