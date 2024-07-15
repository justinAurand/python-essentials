# %% [markdown]
# # Functions as Variables

# %%
# x = 5
def x():
    return 5
print(x)

# %% [markdown]
# ## Viewing Function Data

# %%
print(x.__code__.co_varnames)
print(x.__code__.co_code)

# %% [markdown]
# ## Lambda Functions

# %%
(lambda x: x + 3)(5)

# %%
myList = [5,4,3,2]
sorted(myList)

# %%
myList = [{'num': 3}, {'num': 2}, {'num': 1}]
sorted(myList, key=lambda x: x['num'])


