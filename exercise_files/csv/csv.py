# %%
import csv

# %% [markdown]
# # CSV

# %% [markdown]
# ## Reading

# %%
with open('us.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)

# %%
with open('us.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        print(row)

# %%
with open('us.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        print(row)

# %% [markdown]
# ## Filtering

# %%
with open('us.csv', 'r') as f:
    data = list(csv.DictReader(f, delimiter='\t'))

# %%
primes = []
for number in range (2, 99999):
    for factor in primes:
        if number % factor == 0:
            break
    else:
        primes.append(number)

# %%
filteredData = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']
print(len(data))
print(len(filteredData))

# %% [markdown]
# ## Writing

# %%
with open('10_02_ma_prime.csv', 'w') as f:
    writer = csv.writer(f)
    for row in filteredData:
        writer.writerow([row['place name'], row['county']])
