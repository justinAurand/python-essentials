from tester import Tester

# Triangle Helper
def triangle(num):
    if num == 1 or num == 0:
        return num
    return num + triangle(num - 1)

# Triangle test cases
testInputsAndExpectedResults = [
    (1, 1), # triangle
    (2, 3), # traingle + 1
    (3, 6), # triangle + 3
    (4, 10), # triangle + 6
    (5, 15), # triangle + 10
]

# Test Triangle
tester = Tester(testInputsAndExpectedResults, triangle)
tester.execute()

# Square solution
def square(num):
    if num == 0:
        return num
    return triangle(num) + triangle(num - 1)

# Square test cases
testInputsAndExpectedResults = [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
]

# Test Square
tester = Tester(testInputsAndExpectedResults, square)
tester.execute()
