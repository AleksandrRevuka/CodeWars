from decimal import Decimal


def sum_strings(x, y):
    
    return str(int(Decimal(x)) + int(Decimal(y)))


if __name__ == '__main__':
    print(sum_strings("2108162", "1"))