# %% [markdown]
# # Tuples and Sets

# %% [markdown]
# ## Sets

# %%
mySet = {'a', 'b', 'c'}
print(mySet)

# %%
mySet = set(('a', 'b', 'c'))
print(mySet)

# %%
myList = ['a', 'b', 'b', 'c', 'c']
myList = list(set(myList))
print(myList)

# %%
number = (1,)
print(number[0])

# %%
mySet = set(('a', 'b', 'c'))
mySet.add('d')
print('d' in mySet and 'z' in mySet)
print(len(mySet))

# %%
while len(mySet):
    print(mySet.pop())

# %%
mySet = {'a', 'b', 'c'}
mySet.discard('a')
print(mySet)

# %% [markdown]
# ## Tuples

# %%
myTuple = ('a', 'b', 'c')
print(myTuple)

# %%
print(myTuple[0])

# %%
def returnsMultipleValues():
    return 1,2,3

type(returnsMultipleValues())

# %%
myTuple = 1,2,3
print(type(myTuple))

# %%
print(returnsMultipleValues())

# %%
a, b, c = returnsMultipleValues()
print(a)
print(b)
print(c)
