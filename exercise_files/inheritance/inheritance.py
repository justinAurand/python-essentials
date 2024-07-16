# %% [markdown]
# # Class Inheritance

# %%
class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} says: Bark!')

    def getLegs(self):
        return self._legs

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says Yap yap yap!!!')

    def wagTail(self):
        print('<Vigorous wagging>')

dog = Chihuahua('Roxy')
dog.speak()
dog.wagTail()

myDog = Dog('Rover')
myDog.speak()

# %% [markdown]
# ## Extending built-in classes

# %%
class UniqueList(list):
    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List!'

    def append(self, item):
        if item in self:
            return
        super().append(item)

uniqueList = UniqueList()
print(uniqueList.someProperty)
