from tester import Tester

# Triangle Helper
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

# Triangle test cases
testInputsAndExpectedResults = [
    (1, 1),
    (2, 3),
]

# Test Triangle
tester = Tester(testInputsAndExpectedResults, triangle)
tester.execute()

# Square solution
def square(num):
    return num

# Squre test cases
testInputsAndExpectedResults = [
    (1, 1),
]

# Test Square
tester = Tester(testInputsAndExpectedResults, square)
tester.execute()
