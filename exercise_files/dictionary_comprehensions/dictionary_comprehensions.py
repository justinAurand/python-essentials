# %% [markdown]
# # Dictionary Comprehensions

# %%
animalList = [
    ('a', 'aardvark'),
    ('b', 'bear'),
    ('c', 'cat'),
    ('d', 'dog'),
]
print(animalList)

# %%
animals = {item[0]: item[1] for item in animalList}
print(animals)

# %%
animals = {key: value for key, value in animalList}
print(animals)

# %%
print(animals.items())

# %%
print(list(animals.items()))

# %%
print([{'letter': key, 'name': value} for key, value in animals.items()])
