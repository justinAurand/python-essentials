# %% [markdown]
# # Strings

# %%
import math

# %% [markdown]
# ## Slicing

# %%
name = 'My name is Ryan Mitchell'
name[0]

# %%
name[0:7]
name[:7]

# %%
name[16:]

# %%
myList = [1,2,3,4,5]
myList[2:4]

# %%
len(name)

# %%
len(myList)

# %% [markdown]
# ## Formatting

# %%
'justin ' + 'rules'

# %%
'My number is: ' + str(5)

# %%
f'My number is {5}'

# %%
f'My number is: {5} and twice that is {5*2}'

# %%
f'Pi is: {math.pi:.2f}'

# %%
'Pi is: {}'.format(math.pi)

# %% [markdown]
# ## Multi-line

# %%
myString = '''
I wanted
to include
newlines
in this string
using \'\'\'
'''
print(myString)


# %%
myString
