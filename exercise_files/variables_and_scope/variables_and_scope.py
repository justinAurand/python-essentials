# %% [markdown]
# # Function Scope

# %% [markdown]
# ## locals()

# %%
def performOperation(num1, num2, operation='sum'):
    print(locals())

performOperation(1, 2, 'sum')

# %% [markdown]
# ## globals()

# %%
globals()

# %% [markdown]
# ## Global and Local scope

# %%
message = 'message'
varA = 2

def function1(varA, varB):
    print(varA)
    print(locals())
    print(message)
    def inner_function(varA, varV):
        print(f'inner_function local scope: {locals()}')
    print(locals())
    inner_function(123, 456)

def function2(varC, varD):
    print(varA)
    print(locals())
    print(message)

function1(1, 2)
function2(3, 4)
