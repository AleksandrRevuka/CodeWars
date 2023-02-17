import pytest
from codewar import row_sum_odd_numbers

def main():
    test.assert_equals(row_sum_odd_numbers(1), 1)
    test.assert_equals(row_sum_odd_numbers(2), 8)
    test.assert_equals(row_sum_odd_numbers(13), 2197)
    test.assert_equals(row_sum_odd_numbers(19), 6859)
    test.assert_equals(row_sum_odd_numbers(41), 68921)


if __name__ == '__main__':
    pytest.main()
