# %% [markdown]
# # Data Structures

# %% [markdown]
# ## Lists

# %%
my_list = [1,2,3,4]
print(my_list)

# %%
my_list = [[1,2,3,4], ['list','of','strings'], [True,False]]
len(my_list)

# %%
len(my_list[1])

# %% [markdown]
# ## Sets

# %%
my_set = {1,2,3,4,5}
print(my_set)

# %%
type(my_set)

# %%
len(my_set)

# %%
my_set = {1,1,2,2}
print(my_set)

# %%
[1,2] == [2,1]

# %%
{1,2} == {2,1}

# %% [markdown]
# ## Tuples

# %%
my_tuple = (1,2,3)
len(my_tuple)

# %%
(1,2) == (2,1)

# %%
my_list.append(4)
print(my_list)

# %%
# Tuples are immutable -> my_tuple.append(4) won't work

# %% [markdown]
# ## Dictionaries

# %%
my_dict = {
    'apple': 'a red fruit',
    'bear': 'very gay animal'
}
print(my_dict['apple'])

# %%
my_dict = {
    'apple': 'a red fruit',
    'bear': 'very gay animal',
    'apple': 'sometimes a green fruit'
}
print(my_dict['apple'])

# %%
# this language knows how to equate dictionaries to determine if they're identical, that's great
my_dict2 = {
    'apple': 'a red fruit',
    'bear': 'very gay animal',
    'apple': 'sometimes a green fruit',
    'turd': 'digested food log'
}
print(my_dict == my_dict2)
