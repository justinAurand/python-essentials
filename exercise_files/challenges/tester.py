from typing import Callable

class Tester:
    """
    A class for running multiple unit tests against a system

    Parameter testInputsAndExpectedResults: the list of tests
    Precondition: each test is a tuple containing 1) the input and 2) the expected result

    Parameter sot: the system under test
    Precondition: sot is a function
    """
    def __init__(self, testInputsAndExpectedResults: list[tuple], sot: Callable):
        self.testInputsAndExpectedResults = testInputsAndExpectedResults
        self.sot = sot

    # Run the tests
    def execute(self):
        print(f'{self.sot.__name__}()')
        for testInputAndExpectedResult in self.testInputsAndExpectedResults:
            # Arrange
            input, expectedResult = testInputAndExpectedResult

            # Act
            print(f'Testing case {input}')
            result = self.sot(input)

            # Assert
            if result == expectedResult:
                print('Pass!')
            else:
                print(f'Expected {expectedResult} but received {result}')
                break
        else:
            print(f'{self.sot.__name__}() is correct')
