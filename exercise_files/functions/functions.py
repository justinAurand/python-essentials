# %% [markdown]
# # Functions

# %%
print('Hello, World!')

# %%
def triple(integer):
    return 3 * integer
print(triple(12))

# %%
def multiply(val1, val2):
    return val1 * val2
print(multiply(21,2))

# %%
a = [1,2,3]

def appendFour(myList):
    myList.append(4)

appendFour(a)
print(a)

# %%
type(None)
