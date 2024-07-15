# %% [markdown]
# # Functions

# %%
import math

# %% [markdown]
# ## Named Params

# %%
def performOperation(num1, num2, operation='sum', message='default'):
    print(message)
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2

print(performOperation(2, 3, message='hmph', operation='multiply'))

# %% [markdown]
# ## *args

# %%
def performOperation(*args):
    print(args)

performOperation(1,2,3,4,5)

# %% [markdown]
# ## **kwargs

# %%
def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)

performOperation(1,2,3,4,5, operation='sum', meatball='yum')

# %%
def performOperation(*args, operation='sum'):
    if operation == 'sum':
        return math.sum(args)
    if operation == 'multiply':
        return math.prod(args)

print(performOperation(2, 3, operation='multiply'))
