# %% [markdown]
# # Other Numbers

# %%
from decimal import Decimal, getcontext

# %% [markdown]
# ## Integers

# %%
int('100')

# %%
int('100', 2)

# %%
int('1ab', 16)

# %% [markdown]
# ## Decimals

# %%
getcontext().prec = 2
getcontext()
Decimal(1) / Decimal(3)

# %%
getcontext().prec = 4
getcontext()
Decimal(1) / Decimal(3)

# %%
Decimal(3.14)

# %%
Decimal('3.14')
