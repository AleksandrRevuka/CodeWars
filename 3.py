
def last_digit__(lst: list):
    if not lst:
        return 1

    result = lst[-1]
    memory = {}
    for exp in reversed(lst[:-1]):
        root = f"{exp}_in_{result}"
        if root in memory:
            result = memory[root]
        else:
            result = pow(exp, result)
            memory.update({root: result})
    return result % 10

def last_digit_(lst):
    if not lst:
        return 1

    result = 1
    for x in reversed(lst):
        result = pow(x, result)

    return result % 10

def mod_power(x, y, mod):
    result = 1
    x = x % mod
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % mod
        y = y // 2
        x = (x * x) % mod
    return result

def last_digit(lst: list):
    if not lst:
        return 1

    result = lst[-1]
    for x in reversed(lst[:-1]):
        result = mod_power(x, result, 10)

    return result % 10

if __name__ == '__main__':
    # test_data = (
    #         ([], 1),
    #         ([0, 0], 1),
    #         ([0, 0, 0], 0),
    #         ([1, 2], 1),
    #         ([3, 4, 5], 1),
    #         ([4, 3, 6], 4),
    #         ([7, 6, 21], 1),
    #         ([12, 30, 21], 6),
    #         ([2, 2, 2, 0], 4),
    #         ([937640, 767456, 981242], 0),
    #         ([123232, 694022, 140249], 6),
    #         ([499942, 898102, 846073], 6)
    #     )
    # for test_input, test_output in test_data:
    #     assert last_digit(test_input) == test_output
    
    test_data = [3, 4, 2]
    print(last_digit(test_data))