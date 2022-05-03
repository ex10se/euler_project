def euler_1(n=1000):
    result = 0
    for i in range(1, n):
        if not i % 3 or not i % 5:
            result += i
    return result  # n=1000, result=233168


def euler_2(n):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib(i):
        return i if i in [1, 2] else fib(i - 2) + fib(i - 1)

    result = 0
    x = 1
    while True:
        f = fib(x)
        if f > n:
            break
        if not f % 2:
            result += fib(x)
        x += 1
    return result  # n=4_000_000, result=4613732


if __name__ == '__main__':
    print(euler_2(4_000_000))
