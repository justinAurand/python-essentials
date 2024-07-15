# %%
from collections import defaultdict

# %% [markdown]
# # Dictionaries

# %%
animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat',
}
print(animals)

# %%
print(animals['a'])

# %%
animals['d'] = 'dog'
print(animals)

# %%
animals['a'] = 'antelope'
print(animals)

# %%
print(animals.keys())
print(animals.values())
print(animals.items())

# %%
myList = list(animals.keys())
print(myList)

# %%
print(animals.get('e'))
print(animals.get('e', 'elephant'))

# %%
print(len(animals))

# %%
animals = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
}
animals['b'].append('bison')
print(animals)

# %%
if 'c' not in animals:
    animals['c'] = []
animals['c'].append('cat')
print(animals)

# %% [markdown]
# ## Default

# %%
animals = defaultdict(list)
print(animals)

# %%
animals['e'].append('elephant')
print(animals)

# %%
animals['e'].append('emu')
print(animals)

# %%
print(animals['f'])
