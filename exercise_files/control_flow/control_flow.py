# %% [markdown]
# # Control Flow

# %% [markdown]
# ## If/Else Statements

# %%
a = []
if a:
    print('it is True')
    print('also print this')
else:
    print('it is false')
print('always print me')

# %%
a = True
b = True
if a:
    print('it is True')
    print('also print this')
    if b:
        print('both are True')
else:
    print('it is false')
print('always print me')

# %% [markdown]
# ## For Loops

# %%
a = {1,2,3,4,5}
for item in a:
    print(item)
print(4 in a)
print(type(a))
print(a)

# %% [markdown]
# ## While Loops

# %%
a = 0
while a < 5:
    print(a)
    a = a + 1


