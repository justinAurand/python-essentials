# %% [markdown]
# # If Statements w/ FizzBuzz

# %% [markdown]
# ## Elif Statements

# %%
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16
for n in range(1, 31):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)

# %% [markdown]
# ## Single Line if Statements

# %%
n = 3
fizzBuzz = 'Fizz' if n % 3 == 0 else n
print(fizzBuzz)

# %%
fizzBuzz = ['FizzBuzz' if n % 15 == 0 else 'Buzz' if n % 5 == 0 else 'Fizz' if n % 3 == 0 else n for n in range (1, 31)]
print(fizzBuzz)
