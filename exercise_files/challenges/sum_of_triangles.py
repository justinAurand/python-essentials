from tester import Tester

# Solution
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    pass

# Place test cases here
testInputsAndExpectedResults = [
    (1, 1),
    (2, 3),
]

# Test
tester = Tester(testInputsAndExpectedResults, triangle)
tester.execute()
