# %% [markdown]
# # While

# %%
from datetime import datetime

# %%
print(datetime.now())
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)

# %%
# For 4 seconds into the future, 58 + 5 needs to become 3, not 63
(print(datetime.now().second + 5 % 60))

# %%
wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
    print('Still waiting...')
print(f'We are at {wait_until} seconds!')


# %% [markdown]
# ## Pass

# %%
wait_until2 = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until2:
    pass
print(f'We are at {wait_until2} seconds!')

# %% [markdown]
# ## Break

# %%
wait_until3 = (datetime.now().second + 2) % 60

while True:
    if datetime.now().second == wait_until3:
        print(f'We are at {wait_until3} seconds!')
        break

# %% [markdown]
# ## Continue

# %%
wait_until4 = (datetime.now().second + 2) % 60

while True:
    if datetime.now().second < wait_until4:
        continue
    break
print(f'We are at {wait_until4} seconds!')
