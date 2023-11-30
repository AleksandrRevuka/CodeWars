import asyncio
from concurrent.futures import ThreadPoolExecutor

async def last_digit_(lst: list):
    loop = asyncio.get_running_loop()
    if not lst:
        return 1

    result = lst[-1]
    for x in reversed(lst[:-1]):
        result = pow(x, result)

    return result % 10

def last_digit(lst: list):
    result = asyncio.run(last_digit_(lst))
    return result