# %% [markdown]
# # Class

# %% [markdown]
# ## Instance/Self Attributes

# %%
class Dog:
    _legs = 4 # Instance attribute
    def __init__(self, name):
        self.name = name # Self attribute

    def getLegs(self):
        return self._legs

    def speak(self):
        print(f'{self.name} says: Bark!')

dog = Dog('Kevin')
dog._legs = 3
print(dog.name)
print(dog.getLegs())
print(Dog._legs)


