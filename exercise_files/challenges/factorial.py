from tester import Tester

# Solution
def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1

    value = 1
    number = num
    while number > 1:
        value = value * number
        number = number - 1

    return value

# Place test cases here
testInputsAndExpectedResults = [
    (5, 120)
    ,(5, 120)
    ,(6, 720)
    ,(0, 1)
    ,(-2, None)
    ,(1.2, None)
    ,('spam spam spam', None)
]

# Test
tester = Tester(testInputsAndExpectedResults, factorial)
tester.execute()
