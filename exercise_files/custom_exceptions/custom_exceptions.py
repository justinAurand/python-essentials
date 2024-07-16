# %% [markdown]
# # Custom Exceptions

# %%
class CustomerException(Exception):
    pass

def causeError():
    raise CustomerException('causeError function called')

# causeError()

# %% [markdown]
# ## Adding Attributes

# %%
class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'

class ServerError(HttpException):
    statusCode = 500
    message = 'Server error'

def raiseServerError():
    raise ServerError()

raiseServerError()
