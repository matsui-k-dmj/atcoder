import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from collections import defaultdict
d = defaultdict(list)

import operator
from functools import reduce


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


# from itertools import combinations
# comb = combinations(range(N), 2)

# 累積和
# from itertools import accumulate
# _list = list(accumulate(a_list)

# from functools import lru_cache
# @lru_cache(maxsize=None)
# def setUp(self):
#     dp.cache_clear()


def divisor(n: int):
    """1からsqrt(n)までの約数を全部返す
    
    Args:
        n (int): [description]
    
    Yields:
        int: [description]
    """
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i


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
        while (n % i == 0):
            res[i] += 1
            n = n // i

    if (n != 1):
        res[n] = 1

    return res


def flatten_key_count(d):
    """keyとcountのdictをflattenする
    
    Args:
        d (dict[any, int]): [description]
    
    Returns:
        List[any]: [description]
    """
    return sum([[k for _ in range(d[k])] for k in d.keys()], [])


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    if N == 1:
        print(1)
        return

    _min = 10**10
    for a in divisor(N):
        b = N // a

        if a > b:
            _min = min(_min, len(str(a)))
        else:
            _min = min(_min, len(str(b)))

    print(_min)


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """10000"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000003"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9876543210"""
        output = """6"""
        self.assertIO(input, output)
