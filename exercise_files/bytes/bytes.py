# %% [markdown]
# # Bytes

# %%
bytes(4)

# %%
shockedBytes = bytes('😳', 'utf-8')
shockedBytes

# %%
print(shockedBytes.decode('utf-8'))

# %%
roflBytes = bytearray('🤣', 'utf-8')
roflBytes

# %%
roflBytes[3] = int('85', 16)

# %%
roflBytes.decode('utf-8')
