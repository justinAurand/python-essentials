from tester import Tester

hexNumbers = {
    '0': 0
    ,'1': 1
    ,'2': 2
    ,'3': 3
    ,'4': 4
    ,'5': 5
    ,'6': 6
    ,'7': 7
    ,'8': 8
    ,'9': 9
    ,'A': 10
    ,'B': 11
    ,'C': 12
    ,'D': 13
    ,'E': 14
    ,'F': 15
}

# Solution
def hex_to_dec(hexNum: str):
    if type(hexNum) != str:
        return None

    placeMultiplier = 1
    result = 0
    for char in reversed(hexNum):
        charValue = 0
        try:
            charValue = hexNumbers[char]
        except:
            return None

        charWithPlaceValue = charValue * placeMultiplier
        result = result + charWithPlaceValue
        placeMultiplier = 16 if placeMultiplier == 1 else placeMultiplier ** 2

    return result

# Place test cases here
testInputsAndExpectedResults = [
    ('A2', 162)
    ,('spam spam spam', None)
    ,('A', 10)
    ,('0', 0)
    ,('1B', 27)
    ,('AFC', 2812)
    ,('SC0', None)
    ,('A6G', None)
    ,('ZZT0P', None)
]

# Test
tester = Tester(testInputsAndExpectedResults, hex_to_dec)
tester.execute()
