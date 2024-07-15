# %% [markdown]
# # Lists

# %% [markdown]
# ## Slicing

# %%
myList = [1,2,3,4,5]
myList[3:]

# %%
# step size of 2
myList[0:5:2]

# %%
myList[0:5:3]

# %%
myList[::2]

# %%
for i in range(10):
    print(i)

# %%
myList = list(range(10))
print(myList[::5])

# %%
print(myList[::-2])

# %% [markdown]
# ## Modifying

# %%
myList = [1,2,3,4]
myList.append(5)
print(myList)

# %%
myList.insert(3, 'injection')
print(myList)

# %%
myList.remove('injection')
print(myList)

# %%
print(myList.pop())


# %%
while len(myList):
    print(myList.pop())

# %%
print(myList)

# %%
# referencce
a = [1,2,3,4,5]
b = a
a.append(6)
print(b)

# %%
# value
a = [1,2,3,4,5]
b = a.copy()
a.append(6)
print(b)
