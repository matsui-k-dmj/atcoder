"""
F - Simple Operations on Sequence https://atcoder.jp/contests/abc232/tasks/abc232_f

並べ替えるのはbitDP

ある数より大きい数の集合はO(1)で取れる intersectionもO(1)

{1, ..., N} を並び変えてるとき、
|S| と, j not in S の位置の差は, k < j のうち、k not in S な要素の数

size はちょっと遅いから注意!

"""
import sys
# sys.setrecursionlimit(42000000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

# sにiを追加
def add(s, i):
    return s | (1 << i)

# sからiを除外
def remove(s, i):
    return s & ~(1 << i)

# sにiが入ってるか
def include(s, i):
    return (s >> i) & 1

def size(s):
    return bin(s).count("1")

# i より小さい要素がすべて入った集合
def get_lower(i):
    return (1 << i) - 1

def resolve():
    N, X, Y = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    b_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    
    lower_sets = [get_lower(i) for i in range(N)]

    dp = [float('inf')] * (1 << N) 
    dp[0] = 0
    for s in range((1 << N) - 1):
        s_size = size(s)
        for i in range(N):
            if include(s, i):
                continue

            cost = Y * size(lower_sets[i] & ~s) + X * abs(a_list[i] - b_list[s_size])

            dp[add(s, i)] = min(dp[add(s, i)], dp[s] + cost)

    print(dp[(1 << N) - 1])

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
        input = """4 3 5
4 2 5 2
6 4 2 1"""
        output = """16"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 12345 6789
1 2 3 4 5
1 2 3 4 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """18 20719114 5117250357733867
10511029 36397527 63027379 44706927 47672230 79861204 57882493 42931589 51053644 52300688 43971370 26515475 62139996 41282303 34022578 12523039 6696497 64922712
14720753 4621362 25269832 91410838 86751784 32741849 6602693 60719353 28911226 88280613 18745325 80675202 34289776 37849132 99280042 73760634 43897718 40659077"""
        output = """13104119429316474"""
        self.assertIO(input, output)


