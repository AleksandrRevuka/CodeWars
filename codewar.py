from string import ascii_uppercase


def row_sum_odd_numbers(number):
    return sum(number ** 2 + number - 1 - i * 2 for i, _ in enumerate(range(number)))


def solution(s):
    return ''.join([' ' + symbol if symbol in ascii_uppercase else symbol for i, symbol in enumerate(s)])


if __name__ == '__main__':
    print(row_sum_odd_numbers(4))

    print(solution('breakCamelCase'))


    