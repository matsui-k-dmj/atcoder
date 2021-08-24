import math


def divisor(n: int):
    """1からsqrt(n)までの約数を全部返す
    小さいほうの約数だけが返るので、大きいほうを出す必要があれば割る
    2乗根に注意する

    Args:
        n (int): [description]

    Yields:
        int: [description]
    """
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i


import math
from collections import defaultdict


def prime_factor(n: int):
    """素因数分解

    Args:
        n (int): [description]

    Returns:
        [type]: [description]
    """
    res = defaultdict(int)
    res[1] = 1
    for i in range(2, math.ceil(math.sqrt(n))):
        while n % i == 0:
            res[i] += 1
            n = n // i

    if n != 1:
        res[n] = 1

    return res
