# %% [markdown]
# # List Comprehensions

# %%
myList = [1,2,3,4,5]
doubledList = [2*item for item in myList]
print(doubledList)

# %% [markdown]
# ## Filters

# %%
myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
filteredList.append(100)
print(filteredList)

# %% [markdown]
# ## Functions

# %%
myString = 'My name is Ryan Mitchell. I live in Boston.'
print(myString.split())

# %%
def cleanWord(word):
    return word.replace('.', '').lower()
print(cleanWord(myString))

# %%
cleanWords = [cleanWord(word) for word in myString.split()]
print(cleanWords)

# %%
shortWords = [word for word in cleanWords if len(word) < 3]
print(shortWords)

# %% [markdown]
# ## Nested

# %%
[[cleanWord(word) for word in sentence.split()] for sentence in myString.split('.')]
