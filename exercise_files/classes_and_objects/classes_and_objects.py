# %% [markdown]
# # Classes and Objects

# %% [markdown]
# ## Classes

# %%
class Dog:
    # I'm surprised it's public get/set by default... I thought I liked this language :(
    def __init__(self, name='Rover'):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

my_dog = Dog()
my_dog.speak()
print(my_dog.name)
my_dog.name = 'breakfast'
print(my_dog.name)

# %%
my_dog = Dog()
another_dog = Dog('Fluffy')
print(my_dog.name + ' is chillin with ' + another_dog.name)
