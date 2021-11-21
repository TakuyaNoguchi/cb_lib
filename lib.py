import math

# 10進数 -> base進数に変換
def base10to(x: int, base: int) -> str:
    s = ''

    while x > 0:
        s = str(x % base) + s
        x = x // base

    return s

# 最小公倍数
def lcm(a: int, b: int) -> int:
    return int(a * b  / math.gcd(a, b))

# n以下の素数の一覧
def make_primes(n: int) -> list:
    is_prime = [False, False] + ([True] * (n + 1))

    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]: continue

        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]
