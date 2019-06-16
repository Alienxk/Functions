from pytest import mark
from unittest import TestCase, main


def sum(x: int, y: int) -> int:
    return abs(x + y)

'''
# unittest
class TestSum(TestCase):
    def test_sum__parameterized_testing(self):
        # Fixture
        cases = [(1, 2, 3), (-2, 5, 3), (0, 0, 0),
                 (-1, -1, -2), (1, -2, -1), (10**0, + 1, 2)]

        for x, y, expected in cases:
            with self.subTest(f'Failed in: {x}+{y}={expected}'):
                # Exercise
                result = sum(x, y)

                # Assert
                self.assertEqual(result, expected)

    def test_fake_fail(self):
        self.assertEqual(True, False)

    def test_fake_pass(self):
        self.assertEqual(True, True)


main(verbosity=2)
'''

'''
# pytest -v
@mark.parametrize('x, y, expected',
                  [(1, 2, 3), (-2, 5, 3), (0, 0, 0),
                   (-1, -1, -2), (1, -2, -1), (10**0, + 1, 2)])
def test_sum__parameterized_testing(x, y, expected):
    # Exercise
    result = sum(x, y)

    # Assert
    assert result == expected
'''
