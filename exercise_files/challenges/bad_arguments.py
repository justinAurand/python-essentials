class NonIntArgumentException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) != int:
                raise NonIntArgumentException
        return func(*args)
    return wrapper

@handleNonIntArguments
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1.5, 'foo', 3)
    print('Error: Allowed non-int argument(s)')
except NonIntArgumentException:
    print('Pass!')
except Exception:
    print('Unexpected Exception, expected NonIntArgumentException')

inputsAndExpectedResults = [
    ((1, 2, 3), 6),
]
for inputAndExpectedResult in inputsAndExpectedResults:
    input, expectedResult = inputAndExpectedResult
    result = None
    try:
        result = sum(*input)
    except NonIntArgumentException:
        print('Unexpected NonIntArgumentException, expected no exception')
    except Exception:
        print('Unexpected Exception, expected no exception')
    print('Pass!') if result == expectedResult else print(f'Expected {expectedResult} but received {result}')
