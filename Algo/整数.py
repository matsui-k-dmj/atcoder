"""
コードテストで速度測定済！PythonによるAtCoderスニペット集 (1)基本編 - Qiita https://qiita.com/toast-uz/items/f7a9f586853300732a2b#3-%E6%95%B0%E5%AD%A6%E9%96%A2%E6%95%B0
からコピペ

明らかに not my game感があるので、できることを分かったうえで、ライブラリだけ持っとく
"""

import math


def is_prime(n):
    """n の素数判定
    O(sqrt(n))

    Args:
        n (int)

    Returns:
        bool: nが素数か
    """
    if n == 1:
        return False

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def primes(n):
    """エラトステネスの篩
    n以下の素数を求める
    O(nloglogn), max 10**7

    Args:
        n (int)

    Returns:
        List[int]: n以下の素数
    """
    sieve = [True] * ((n + 1) // 2)
    for i in range(1, (int(n ** 0.5) + 1) // 2):
        if sieve[i]:
            for j in range(i * 3 + 1, (n + 1) // 2, i * 2 + 1):
                sieve[j] = False
    res = [i * 2 + 1 for i, s in enumerate(sieve) if s]
    res[0] = 2
    return res


def divisors(n):
    """nの約数を列挙する
    O(sqrt(n))

    Args:
        n (int)

    Returns:
        List[int]: 小さい順にnの約数のリスト
    """
    res_low, res_high = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res_low.append(i)
            if i != n // i:
                res_high.append(n // i)
        i += 1
    return res_low + res_high[::-1]


def prime_factors(n):
    """nの素因数分解
    O(sqrt(n)) <- ワースト. 実際はもっと早い

    Args:
        n (int)

    Returns:
        List[int]: nの素因数
    """
    res = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n // i
            res[i] = res.get(i, 0) + 1
        i += 1
    if n > 1:
        res[n] = res.get(n, 0) + 1
    return res


##### MOD #####

MOD = 1000000007

# べき乗, xのn乗のMOD, O(log n)
# res = pow(x, n, MOD)


def factorial(n, start=1):
    """階乗, factorial
    O(n) or O(n - start), max 10**8

    Args:
        n (int): [description]
        start (int, optional): 階乗のスタート. Defaults to 1.

    Returns:
        int: n! (or n! / (start-1)!)
    """
    if n >= MOD:
        return 0
    val = 1
    for i in range(start, n + 1):
        val = val * i % MOD
    return val


def modinv(a):
    """一般的な a の逆元 (ax = 1 mod MOD を 満たす x)
    MOD がなんでも成り立つ
    O(log n)

    Args:
        a (int)

    Returns:
        int: aの逆元
    """
    b, x, y = MOD, 1, 0
    while b:
        tmp = a // b
        a -= tmp * b
        x -= tmp * y
        a, b, x, y = b, a, y, x
    x %= MOD
    if x < 0:
        x += MOD
    return x


# 逆元: MODが素数でxを割り切らないとき(MODがデカい素数の場合など)、フェルマーの小定理によって
# O(log MOD) 無視できるくらい速い
modinv = lambda n: pow(n, MOD - 2, MOD)


def perm(n, r):
    """nPr: 順列
    O(n - r), max 10**8

    Args:
        n (int)
        r (int)
        MOD (int)

    Returns:
        int: 順列数
    """
    if n >= MOD:
        return 0
    res = 1
    for i in range(n - r + 1, n + 1):
        res = res * i % MOD
    return res


def comb(n, r):
    """nCr: 組み合わせ
    O(n), max 10**8

    nCr = nPr / r!

    Args:
        n (int)
        r (int)

    Returns:
        int: nCr
    """
    return (perm(n, r) * modinv(factorial(r))) % MOD


###　前処理式: 何回もcombなどを求める必要がある場合、先にfactorial だけ計算しとく。
# 一回だけなら前記の関数のほうが単純なので速い
# O(n), max 10**6
# 前処理
MAX_SIZE = 10 ** 6  # nのmax
fact = [0] * (MAX_SIZE + 1)
fact[0] = fact[1] = 1
for i in range(2, MAX_SIZE + 1):
    fact[i] = fact[i - 1] * i % MOD

# 関数定義  n >= MOD や n < r の処理はしていません
factorial = lambda n: fact[n]
modinv = lambda n: pow(n, MOD - 2, MOD)
perm = lambda n, r: factorial(n) * modinv(factorial(n - r)) % MOD
comb = lambda n, r: perm(n, r) * modinv(factorial(r)) % MOD


def fibonacci(n):
    """フィボナッチ数列を求める
    O(n), max 10**7

    Args:
        n (int)

    Returns:
        List[int]: 0 から n番目までの フィボナッチ数列 (MOD)
    """
    fibo = [None] * (n + 1)
    fibo[0], fibo[1] = 0, 1
    for i in range(2, n + 1):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % MOD

    return fibo
