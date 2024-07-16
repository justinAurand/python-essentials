# %% [markdown]
# # Handling Exceptions

# %%
import time

# %% [markdown]
# ## Try / Except

# %%
def causeError():
    try:
        return 1/0
    except Exception as e:
        return e

causeError()

# %% [markdown]
# ## Finally

# %%
def causeError():
    start = time.time()
    try:
        return 1/0
    except Exception as e:
        return e
    finally:
        print(f'function took {time.time() - start} to run')

causeError()

# %% [markdown]
# ## by Type

# %%
def causeError():
    try:
        return 1/0
    except Exception as e:
        print('error')
    except TypeError:
        print('type error')
    except ZeroDivisionError:
        print('zero division error')

causeError()

# %% [markdown]
# ## Custom Decorators

# %%
def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('type error')
        except ZeroDivisionError:
            print('zero division error')
        except Exception:
            print('error')
    return wrapper

@handleException
def causeError():
    return 1/0

causeError()


# %% [markdown]
# ## Raising Exceptions

# %%
@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)

raiseError()
