from typing import List

# 再起限界
import sys
sys.setrecursionlimit(4100000)


# 連続する文字のマックスを取る
def count_raw_char(s, char):
    max_len = 0
    current_len = 0
    for c in s:
        if c == char:
            current_len += 1
        else:
            if max_len < current_len:
                max_len = current_len
            current_len = 0

    return max_len


def ceil_int(a, devider):
    """
    floor は a // devider でいい。
    math.floor(a / divedier)　だとオーバーフローしちゃう。
    """

    if (a % devider > 0):
        a_ceil = a // devider + 1
    else:
        a_ceil = a // devider

    return a_ceil


# 配列の初期化
N0, N1, N2, N3 = 5, 6, 8, 9
a = [0] * N0

b = [[0] * N2 for i in range(N0)]

c = [[[0] * N2 for i in range(N1)] for j in range(N0)]

d = [[[[0] * N3 for i in range(N2)] for i in range(N1)] for j in range(N0)]

# メモ化再帰 (やらないほうがいい)
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n == -1:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# gcd
from fractions import gcd

# 累積和
from itertools import accumulate

a_range = range(1, 11)
b = list(accumulate(a_range))  # type: ignore
print(a)
print(b)