import sys
sys.setrecursionlimit(10**6)

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

    if(a % devider > 0):
        a_ceil = a // devider + 1
    else:
        a_ceil = a // devider

    return a_ceil

def list_matrix(H, W, padding=0):
    return [[padding] * W for _ in range(H)]

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n == -1:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)