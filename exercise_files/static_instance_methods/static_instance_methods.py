# %% [markdown]
# # Static and Instance Methods

# %%
class WordSet:
    # static attribute
    replacePuncs = ['!', '.', ',', '\'']

    def __init__(self):
        # instance attribute
        self.words = set()

    # instance method
    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)

    # static method
    def cleanText(text):
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, '')
        return text.lower()

wordSet = WordSet()

wordSet.addText('Hi, I\'m Ryan')
wordSet.addText('Here\'s more text')

print(wordSet.words)

# %% [markdown]
# # Decorators

# %%
class WordSet:
    # static attribute
    replacePuncs = ['!', '.', ',', '\'']

    def __init__(self):
        # instance attribute
        self.words = set()

    # instance method
    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    @staticmethod
    def cleanText(text):
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, '')
        return text.lower()

wordSet = WordSet()

wordSet.addText('Hi, I\'m Ryan')
wordSet.addText('Here\'s more text')

print(wordSet.words)
