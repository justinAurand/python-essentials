# %% [markdown]
# # Files

# %% [markdown]
# ## Reading

# %%
f = open('10_01_file.txt', 'r')
print(f)

# %%
print(f.readline())

# %%
print(f.readline())

# %%
print(f.readlines())

# %%
f = open('10_01_file.txt', 'r')
for line in f.readlines():
    print(line.strip())

# %% [markdown]
# ## Writing

# %%
f = open('10_01_output.txt', 'a')
print(f)

# %%
f.write('Line 1\n')
f.write('Line 2\n')
f.close()

# %%
with open('10_01_output.txt', 'a') as f:
    f.write('something')
    f.write('something else')
print(f)

# %%
f.write('ps, forgot this')


