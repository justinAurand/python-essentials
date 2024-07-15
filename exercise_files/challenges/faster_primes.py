from tester import Tester

# Solution
def allPrimesUpTo(num: int) -> list:
    primesFound = [2]
    for number in range(2, num):
        for primefactor in primesFound:
            if number % primefactor == 0:
                break
        else:
            primesFound.append(number)
    return primesFound

# Place test cases here
testInputsAndExpectedResults = [
    (3, [2]),
    (4, [2, 3]),
    (10, [2, 3, 5, 7]),
    (100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
           43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
]

# Test
tester = Tester(testInputsAndExpectedResults, allPrimesUpTo)
tester.execute()
