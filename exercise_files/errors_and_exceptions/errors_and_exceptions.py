# %% [markdown]
# # Errors and Exceptions

# %%
def causeError():
    return 1/0

causeError()
    

# %% [markdown]
# ## Try / Except

# %%
def causeError():
    return 1/0

def callCauseError():
    return causeError()

try:
    callCauseError()
except Exception as e:
    print(type(e))
