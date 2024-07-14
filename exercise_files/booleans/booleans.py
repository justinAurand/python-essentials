# %% [markdown]
# # Booleans

# %%
True or False

# %% [markdown]
# ## Casting

# %%
bool(1)

# %%
bool(0)

# %%
bool(-1)

# %%
bool(1j)

# %%
bool(0.0)

# %%
bool(0j)

# %%
bool('False')

# %%
bool('')

# %%
bool(' ')

# %%
bool(())

# %%
bool((1))

# %%
myList = [1,2]
if myList:
    print('myList has stuff in it')

# %%
a = 5
b = 5
if a - b:
    print('a does not equal b')

# %% [markdown]
# ## Logic

# %%
weatherIsNice = False
haveUmbrella = False

if haveUmbrella or weatherIsNice:
    print('go for a walk')
else:
    print('stay inside')


