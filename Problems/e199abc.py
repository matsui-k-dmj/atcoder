"""
E - Permutation https://atcoder.jp/contests/abc199/tasks/abc199_e

状態遷移する前にチェックするのと後でチェックするのだと計算量変わる。

nビット以下の1の個数は, bin(s)[-n:].count(1) な

key が intのときはdictじゃなくてlist使っとけばいいからな

bitDP, ビットDP

dp[s] = sum_x dp[s\{x}] (if c)
みたいなときは、for s in range(1 << N) で, 部分集合から順に列挙できるので、
for i in range(N):
    if c:
        dp[s | {i}] += dp[s]
で良い

N = 18だと、2**N * N = 5 * 10**6 が限界。 2**N * N**2 = 8.5 * 10**7
"""

import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import math
from collections import defaultdict

# sにiを追加
def add(s, i):
    return s | (1 << i)

# sからiを除外
def remove(s, i):
    return s & ~(1 << i)

# sにiが入ってるか
def include(s, i):
    return (s >> i) & 1

# s の要素数
def size(s):
    return bin(s).count("1")

def resolve():

    N, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(M)
    ]  # int grid

    def check(s, y, z):
        return bin(s)[-y:].count("1") <= z

    constraints = [[] for _ in range(N)]
    for x, y, z in grid:
        constraints[x-1].append((y, z))


    dp = [0] * (1 << N)
    dp[0] = 1
    for s in range(1 << N):
        ok = True
        for y, z in constraints[size(s)-1]:
            if not check(s, y, z):
                ok = False
        if not ok:
            continue

        for next_factor in range(N):
            if include(s, next_factor):
                continue
            
            next_s = add(s, next_factor)
            dp[next_s] += dp[s]

    print(dp[-1])

if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py

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
        input = """3 1
2 2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
3 3 2
4 4 3"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """18 0"""
        output = """6402373705728000"""
        self.assertIO(input, output)


