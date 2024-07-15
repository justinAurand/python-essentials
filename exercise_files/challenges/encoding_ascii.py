from tester import Tester

# Encode string solution
def encodeString(stringVal):
    char = ''
    count = 0
    result = []

    for item in stringVal:
        # Handle first iteration
        if not char:
            char = item
            count = 1
            continue

        # Handle matches
        if item == char:
            count = count + 1
            continue

        # Handle mismatches
        result.append((char, count))
        char = item
        count = 1

    # Capture final encode
    result.append((char, count))

    return result

# Place test cases here
testInputsAndExpectedResults = [
    ('AAAAABBBBAAA', [
        ('A', 5),
        ('B', 4),
        ('A', 3),
    ]),
    ('Bookkeeping', [
        ('B', 1),
        ('o', 2),
        ('k', 2),
        ('e', 2),
        ('p', 1),
        ('i', 1),
        ('n', 1),
        ('g', 1),
    ]),
]

# Test
tester = Tester(testInputsAndExpectedResults, encodeString)
tester.execute()

# Decode string solution
def decodeRunLength(runLength) -> str:
    char, count = runLength
    return char * count

def decodeString(encodedList):
    result = ''
    for runLength in encodedList:
        run = decodeRunLength(runLength)
        result = result + run
    return result

# Place test cases here
testInputsAndExpectedResults = [
    ([
        ('A', 5),
        ('B', 4),
        ('A', 3),
    ], 'AAAAABBBBAAA'),
    ([
        ('B', 1),
        ('o', 2),
        ('k', 2),
        ('e', 2),
        ('p', 1),
        ('i', 1),
        ('n', 1),
        ('g', 1),
    ], 'Bookkeeping'),
]

# Test
tester = Tester(testInputsAndExpectedResults, decodeString)
tester.execute()
